/**
 * OMTENTA MODULE - Struktur för Inför Omtenta Linux
 * 7 tasks baserade på de 7 områdena
 */

export interface OmtentaTask {
    id: string
    title: string
    description: string
    flashcardCount: number
    quizCount: number
}

export const OMTENTA_MODULE = {
    id: 'omtenta-linux',
    slug: 'omtenta-linux',
    title: 'Inför Omtenta Linux',
    description: 'Komplett förberedelse för Linux-omtentan',
    icon: '📚',
    color: 'amber',
    tasks: [
        {
            id: 'ssh-brandvagg',
            title: 'SSH & Brandvägg',
            description: 'SSH-konfiguration, nycklar, UFW och iptables',
            flashcardCount: 50,
            quizCount: 50
        },
        {
            id: 'block-storage',
            title: 'Block Storage & Kryptering',
            description: 'LVM, partitioner, LUKS, filsystem',
            flashcardCount: 50,
            quizCount: 50
        },
        {
            id: 'docker',
            title: 'Docker & Kontainrar',
            description: 'Containers, images, volumes, docker-compose',
            flashcardCount: 50,
            quizCount: 50
        },
        {
            id: 'anvandarhantering',
            title: 'Användarhantering',
            description: 'Users, groups, permissions, sudoers',
            flashcardCount: 50,
            quizCount: 50
        },
        {
            id: 'filsystem',
            title: 'Filsystem & Navigation',
            description: 'Paths, FHS, kommandon, rättigheter',
            flashcardCount: 50,
            quizCount: 50
        },
        {
            id: 'pakethantering',
            title: 'Pakethantering & SSH-nycklar',
            description: 'APT, dpkg, repositories, SSH-nycklar',
            flashcardCount: 50,
            quizCount: 50
        },
        {
            id: 'subnetting',
            title: 'Subnetting & Nätverk',
            description: 'IP-adressering, CIDR, subnätberäkning',
            flashcardCount: 50,
            quizCount: 50
        }
    ]
}
