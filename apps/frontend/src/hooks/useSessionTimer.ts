"use client"

/**
 * Session Timer Hook
 * ==================
 *
 * Spårar tid inloggad med veckovis brytpunkt (mån 00:01 - sön 23:59).
 * Sparar i localStorage och resettar automatiskt varje vecka.
 */

import { useState, useEffect, useCallback } from "react"

interface WeeklySession {
    weekStart: string  // ISO date string för veckans måndag
    totalSeconds: number
    dailySessions: {
        [date: string]: number  // ISO date: seconds
    }
}

interface SessionTimerReturn {
    currentSessionSeconds: number
    weeklyTotalSeconds: number
    todaySeconds: number
    weekHistory: WeeklySession[]
    formatTime: (seconds: number) => string
    formatTimeShort: (seconds: number) => string
}

// Få måndagen för given vecka
function getWeekStart(date: Date): string {
    const d = new Date(date)
    const day = d.getDay()
    const diff = d.getDate() - day + (day === 0 ? -6 : 1) // Justera för söndag
    d.setDate(diff)
    d.setHours(0, 0, 0, 0)
    return d.toISOString().split("T")[0]
}

// Få dagens datum som string
function getToday(): string {
    return new Date().toISOString().split("T")[0]
}

const STORAGE_KEY = "devopshub_session_timer"
const HISTORY_KEY = "devopshub_session_history"

export function useSessionTimer(): SessionTimerReturn {
    const [currentSessionSeconds, setCurrentSessionSeconds] = useState(0)
    const [weeklyData, setWeeklyData] = useState<WeeklySession | null>(null)
    const [weekHistory, setWeekHistory] = useState<WeeklySession[]>([])

    // Ladda data vid mount
    useEffect(() => {
        const today = getToday()
        const currentWeekStart = getWeekStart(new Date())

        // Ladda historik
        try {
            const historyStr = localStorage.getItem(HISTORY_KEY)
            if (historyStr) {
                setWeekHistory(JSON.parse(historyStr))
            }
        } catch {
            // Ignorera fel
        }

        // Ladda eller skapa veckodata
        try {
            const savedStr = localStorage.getItem(STORAGE_KEY)
            if (savedStr) {
                const saved: WeeklySession = JSON.parse(savedStr)

                // Kolla om det är ny vecka
                if (saved.weekStart !== currentWeekStart) {
                    // Spara förra veckans data till historik
                    const historyStr = localStorage.getItem(HISTORY_KEY)
                    const history: WeeklySession[] = historyStr ? JSON.parse(historyStr) : []
                    history.unshift(saved) // Lägg till i början
                    // Behåll max 8 veckor
                    const trimmedHistory = history.slice(0, 8)
                    localStorage.setItem(HISTORY_KEY, JSON.stringify(trimmedHistory))
                    setWeekHistory(trimmedHistory)

                    // Ny vecka - ny data
                    const newData: WeeklySession = {
                        weekStart: currentWeekStart,
                        totalSeconds: 0,
                        dailySessions: {}
                    }
                    setWeeklyData(newData)
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(newData))
                } else {
                    setWeeklyData(saved)
                }
            } else {
                // Första gången
                const newData: WeeklySession = {
                    weekStart: currentWeekStart,
                    totalSeconds: 0,
                    dailySessions: {}
                }
                setWeeklyData(newData)
                localStorage.setItem(STORAGE_KEY, JSON.stringify(newData))
            }
        } catch {
            // Vid fel, skapa ny
            const newData: WeeklySession = {
                weekStart: currentWeekStart,
                totalSeconds: 0,
                dailySessions: {}
            }
            setWeeklyData(newData)
        }
    }, [])

    // Timer som räknar uppåt
    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentSessionSeconds(prev => prev + 1)
        }, 1000)

        return () => clearInterval(interval)
    }, [])

    // Spara till localStorage varje minut
    useEffect(() => {
        if (!weeklyData) return

        const saveInterval = setInterval(() => {
            const today = getToday()
            const updatedData: WeeklySession = {
                ...weeklyData,
                totalSeconds: weeklyData.totalSeconds + 60,
                dailySessions: {
                    ...weeklyData.dailySessions,
                    [today]: (weeklyData.dailySessions[today] || 0) + 60
                }
            }
            setWeeklyData(updatedData)
            localStorage.setItem(STORAGE_KEY, JSON.stringify(updatedData))
        }, 60000) // Varje minut

        return () => clearInterval(saveInterval)
    }, [weeklyData])

    // Spara vid unmount/stängning
    useEffect(() => {
        const handleBeforeUnload = () => {
            if (!weeklyData) return
            const today = getToday()
            const sessionMinutes = Math.floor(currentSessionSeconds / 60)
            const updatedData: WeeklySession = {
                ...weeklyData,
                totalSeconds: weeklyData.totalSeconds + sessionMinutes * 60,
                dailySessions: {
                    ...weeklyData.dailySessions,
                    [today]: (weeklyData.dailySessions[today] || 0) + sessionMinutes * 60
                }
            }
            localStorage.setItem(STORAGE_KEY, JSON.stringify(updatedData))
        }

        window.addEventListener("beforeunload", handleBeforeUnload)
        return () => window.removeEventListener("beforeunload", handleBeforeUnload)
    }, [weeklyData, currentSessionSeconds])

    // Formatera tid (timmar:minuter:sekunder)
    const formatTime = useCallback((seconds: number): string => {
        const hrs = Math.floor(seconds / 3600)
        const mins = Math.floor((seconds % 3600) / 60)
        const secs = seconds % 60
        if (hrs > 0) {
            return `${hrs}:${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`
        }
        return `${mins}:${secs.toString().padStart(2, "0")}`
    }, [])

    // Kortare format (t ex "2h 30m")
    const formatTimeShort = useCallback((seconds: number): string => {
        const hrs = Math.floor(seconds / 3600)
        const mins = Math.floor((seconds % 3600) / 60)
        if (hrs > 0) {
            return `${hrs}h ${mins}m`
        }
        if (mins > 0) {
            return `${mins}m`
        }
        return `${seconds}s`
    }, [])

    const today = getToday()
    const todaySeconds = weeklyData?.dailySessions[today] || 0
    const weeklyTotalSeconds = weeklyData?.totalSeconds || 0

    return {
        currentSessionSeconds,
        weeklyTotalSeconds: weeklyTotalSeconds + currentSessionSeconds,
        todaySeconds: todaySeconds + currentSessionSeconds,
        weekHistory,
        formatTime,
        formatTimeShort
    }
}
