import { OmtentaV2Question } from './omtenta-v2-ssh-brandvagg'

export const ANVANDARHANTERING_V2_QUESTIONS: OmtentaV2Question[] = [
  {
    id: 'omtenta-v2-user-1',
    question: 'The root user has UID...',
    options: ['1', '100', '0', '1000'],
    correctIndices: [2],
    explanation: 'The root user always has UID 0 on Linux systems.',
    difficulty: 'G',
    category: 'User IDs',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-2',
    question: 'Regular users typically start at UID...',
    options: ['0', '100', '500', '1000'],
    correctIndices: [3],
    explanation: 'Regular users typically start at UID 1000 on modern Linux systems.',
    difficulty: 'G',
    category: 'User IDs',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-3',
    question: 'User information is stored in...',
    options: ['/etc/users', '/etc/accounts', '/etc/passwd', '/etc/logins'],
    correctIndices: [2],
    explanation: 'User information is stored in /etc/passwd.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-4',
    question: 'Encrypted passwords are stored in...',
    options: ['/etc/passwd', '/etc/passwords', '/etc/shadow', '/etc/secure'],
    correctIndices: [2],
    explanation: 'Encrypted passwords are stored in /etc/shadow for security.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-5',
    question: 'Group information is stored in...',
    options: ['/etc/groups', '/etc/group', '/etc/teams', '/etc/members'],
    correctIndices: [1],
    explanation: 'Group information is stored in /etc/group.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-6',
    question: 'The command to create a user is...',
    options: ['newuser', 'createuser', 'useradd', 'adduser'],
    correctIndices: [2],
    explanation: 'useradd is the standard command to create users in Linux.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-7',
    question: 'The command to delete a user is...',
    options: ['deluser', 'removeuser', 'userdel', 'userdelete'],
    correctIndices: [2],
    explanation: 'userdel is the command to delete users.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-8',
    question: 'The command to modify a user is...',
    options: ['userchange', 'modifyuser', 'usermod', 'changeuser'],
    correctIndices: [2],
    explanation: 'usermod is the command to modify user accounts.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-9',
    question: 'The command to create a group is...',
    options: ['newgroup', 'creategroup', 'groupadd', 'addgroup'],
    correctIndices: [2],
    explanation: 'groupadd is the command to create groups.',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-10',
    question: 'The command to delete a group is...',
    options: ['delgroup', 'removegroup', 'groupdel', 'groupremove'],
    correctIndices: [2],
    explanation: 'groupdel is the command to delete groups.',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-11',
    question: 'To add user to a group, use...',
    options: ['groupadd -u user group', 'addgroup user group', 'usermod -aG group user', 'useradd -g group user'],
    correctIndices: [2],
    explanation: 'usermod -aG group user adds a user to a group while preserving existing groups.',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-12',
    question: 'The -a flag in usermod -aG means...',
    options: ['Admin', 'All', 'Append', 'Add'],
    correctIndices: [2],
    explanation: 'The -a flag means Append, which preserves existing group memberships.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-13',
    question: 'Without -a in usermod -G, the user...',
    options: ['Gets added to the group', 'Loses all other groups', 'Becomes admin', 'Nothing changes'],
    correctIndices: [1],
    explanation: 'Without -a, usermod -G replaces all groups, causing the user to lose other group memberships.',
    difficulty: 'VG',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-14',
    question: 'The command to change password is...',
    options: ['password', 'chpass', 'passwd', 'setpass'],
    correctIndices: [2],
    explanation: 'passwd is the command to change user passwords.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-15',
    question: 'The command to show user ID is...',
    options: ['uid', 'user', 'id', 'whoami'],
    correctIndices: [2],
    explanation: 'The id command shows user ID, group ID, and group memberships.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-16',
    question: 'The command to show current user is...',
    options: ['me', 'user', 'whoami', 'currentuser'],
    correctIndices: [2],
    explanation: 'whoami displays the current username.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-17',
    question: 'The command to show user groups is...',
    options: ['usergroups', 'groups', 'mygroups', 'showgroups'],
    correctIndices: [1],
    explanation: 'The groups command shows the groups a user belongs to.',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-18',
    question: 'The command to switch user is...',
    options: ['switch', 'change', 'su', 'user'],
    correctIndices: [2],
    explanation: 'su (switch user) is used to switch to another user account.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-19',
    question: 'To run command as root, use...',
    options: ['root', 'admin', 'sudo', 'super'],
    correctIndices: [2],
    explanation: 'sudo allows running commands with root privileges.',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-20',
    question: 'sudo stands for...',
    options: ['Super User DO', 'Superuser Do', 'Switch User DO', 'System User Do'],
    correctIndices: [1],
    explanation: 'sudo stands for "Superuser Do".',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-21',
    question: 'The sudoers file is located at...',
    options: ['/etc/sudo', '/etc/sudoers.conf', '/etc/sudoers', '/etc/sudo.conf'],
    correctIndices: [2],
    explanation: 'The sudoers configuration file is located at /etc/sudoers.',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-22',
    question: 'To edit sudoers safely, use...',
    options: ['vim /etc/sudoers', 'nano /etc/sudoers', 'visudo', 'sudoedit'],
    correctIndices: [2],
    explanation: 'visudo should be used to edit sudoers safely with syntax checking.',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-23',
    question: 'Permission r equals...',
    options: ['1', '2', '4', '7'],
    correctIndices: [2],
    explanation: 'Read (r) permission has the numeric value 4.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-24',
    question: 'Permission w equals...',
    options: ['1', '2', '4', '7'],
    correctIndices: [1],
    explanation: 'Write (w) permission has the numeric value 2.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-25',
    question: 'Permission x equals...',
    options: ['1', '2', '4', '7'],
    correctIndices: [0],
    explanation: 'Execute (x) permission has the numeric value 1.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-26',
    question: 'Permission rwx equals...',
    options: ['6', '7', '5', '3'],
    correctIndices: [1],
    explanation: 'rwx = 4 + 2 + 1 = 7.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-27',
    question: 'Permission rw- equals...',
    options: ['5', '6', '7', '4'],
    correctIndices: [1],
    explanation: 'rw- = 4 + 2 + 0 = 6.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-28',
    question: 'Permission r-x equals...',
    options: ['6', '5', '4', '3'],
    correctIndices: [1],
    explanation: 'r-x = 4 + 0 + 1 = 5.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-29',
    question: 'Permission 755 means...',
    options: ['rwxr--r--', 'rw-r-xr-x', 'rwxr-xr-x', 'rwx------'],
    correctIndices: [2],
    explanation: '755 = rwx (7) for owner, r-x (5) for group, r-x (5) for others.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-30',
    question: 'Permission 644 means...',
    options: ['rw-r--r-x', 'rw-r--r--', 'rwxr--r--', 'rw-rw-r--'],
    correctIndices: [1],
    explanation: '644 = rw- (6) for owner, r-- (4) for group, r-- (4) for others.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-31',
    question: 'Permission 700 means...',
    options: ['rw-------', 'r--------', 'rwx------', 'rwxrwxrwx'],
    correctIndices: [2],
    explanation: '700 = rwx (7) for owner, --- (0) for group, --- (0) for others.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-32',
    question: 'Permission 777 means...',
    options: ['rwxrwx---', 'rwxr-xr-x', 'rwxrwxrwx', 'rw-rw-rw-'],
    correctIndices: [2],
    explanation: '777 = rwx (7) for all: owner, group, and others.',
    difficulty: 'G',
    category: 'Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-33',
    question: 'The command to change permissions is...',
    options: ['perm', 'chperm', 'chmod', 'setperm'],
    correctIndices: [2],
    explanation: 'chmod (change mode) is used to change file permissions.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-34',
    question: 'The command to change owner is...',
    options: ['owner', 'setowner', 'chown', 'changeowner'],
    correctIndices: [2],
    explanation: 'chown (change owner) is used to change file ownership.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-35',
    question: 'The command to change group is...',
    options: ['group', 'setgroup', 'chgrp', 'changegroup'],
    correctIndices: [2],
    explanation: 'chgrp (change group) is used to change file group ownership.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-36',
    question: 'chmod +x adds...',
    options: ['Read permission', 'Write permission', 'Execute permission', 'All permissions'],
    correctIndices: [2],
    explanation: 'chmod +x adds execute permission to a file.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-37',
    question: 'chmod -w removes...',
    options: ['Read permission', 'Write permission', 'Execute permission', 'All permissions'],
    correctIndices: [1],
    explanation: 'chmod -w removes write permission from a file.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-38',
    question: 'chmod u+x adds execute for...',
    options: ['Group', 'Others', 'User/owner', 'Everyone'],
    correctIndices: [2],
    explanation: 'u stands for user/owner, so chmod u+x adds execute for the owner.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-39',
    question: 'chmod g+w adds write for...',
    options: ['User', 'Group', 'Others', 'Everyone'],
    correctIndices: [1],
    explanation: 'g stands for group, so chmod g+w adds write for the group.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-40',
    question: 'chmod o-r removes read for...',
    options: ['User', 'Group', 'Others', 'Everyone'],
    correctIndices: [2],
    explanation: 'o stands for others, so chmod o-r removes read for others.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-41',
    question: 'chmod a+x adds execute for...',
    options: ['User only', 'Group only', 'Others only', 'All (everyone)'],
    correctIndices: [3],
    explanation: 'a stands for all, so chmod a+x adds execute for everyone.',
    difficulty: 'G',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-42',
    question: 'The SUID bit value is...',
    options: ['1000', '2000', '4000', '8000'],
    correctIndices: [2],
    explanation: 'The SUID (Set User ID) bit has the numeric value 4000.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-43',
    question: 'The SGID bit value is...',
    options: ['1000', '2000', '4000', '8000'],
    correctIndices: [1],
    explanation: 'The SGID (Set Group ID) bit has the numeric value 2000.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-44',
    question: 'The sticky bit value is...',
    options: ['1000', '2000', '4000', '8000'],
    correctIndices: [0],
    explanation: 'The sticky bit has the numeric value 1000.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-45',
    question: 'SUID on a file means...',
    options: ['Anyone can execute', 'Runs as file owner', 'Inherits group', 'Cannot be deleted'],
    correctIndices: [1],
    explanation: 'SUID causes the file to run with the permissions of the file owner.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-46',
    question: 'SGID on a directory means...',
    options: ['Anyone can enter', 'Runs as owner', 'New files inherit group', 'Cannot be deleted'],
    correctIndices: [2],
    explanation: 'SGID on a directory causes new files to inherit the group of the directory.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-47',
    question: 'Sticky bit on a directory means...',
    options: ['Files are permanent', 'Files are hidden', 'Only owner can delete own files', 'Files are encrypted'],
    correctIndices: [2],
    explanation: 'The sticky bit prevents users from deleting files owned by others.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-48',
    question: 'The /tmp directory has sticky bit to...',
    options: ['Make files permanent', 'Hide files', 'Prevent users deleting others\' files', 'Encrypt files'],
    correctIndices: [2],
    explanation: '/tmp has the sticky bit to prevent users from deleting each other\'s temporary files.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-49',
    question: 'chmod 2770 sets...',
    options: ['SUID + rwxrwx---', 'SGID + rwxrwx---', 'Sticky + rwxrwx---', 'rwxrwxrwx'],
    correctIndices: [1],
    explanation: 'The leading 2 sets SGID, and 770 gives rwxrwx--- permissions.',
    difficulty: 'VG',
    category: 'Special Permissions',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-50',
    question: 'Select all that are permission commands (choose 3):',
    options: ['chmod', 'perm', 'chown', 'setperm', 'chgrp', 'changeperm', 'modperm', 'groupperm', 'userperm', 'fileperm'],
    correctIndices: [0, 2, 4],
    explanation: 'chmod, chown, and chgrp are the three permission-related commands.',
    difficulty: 'VG',
    category: 'Permission Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-51',
    question: 'A user\'s home directory is usually...',
    options: ['/user/name', '/users/name', '/home/name', '/home/users/name'],
    correctIndices: [2],
    explanation: 'User home directories are located in /home/username.',
    difficulty: 'G',
    category: 'Home Directory',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-52',
    question: 'The root user\'s home is...',
    options: ['/home/root', '/root', '/', '/admin'],
    correctIndices: [1],
    explanation: 'The root user\'s home directory is /root.',
    difficulty: 'G',
    category: 'Home Directory',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-53',
    question: 'To create user with home directory, use...',
    options: ['useradd -h', 'useradd -d', 'useradd -m', 'useradd -home'],
    correctIndices: [2],
    explanation: 'useradd -m creates the user\'s home directory.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-54',
    question: 'To specify home directory path, use...',
    options: ['useradd -h /path', 'useradd -d /path', 'useradd -m /path', 'useradd -home /path'],
    correctIndices: [1],
    explanation: 'useradd -d specifies the home directory path.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-55',
    question: 'To specify user\'s shell, use...',
    options: ['useradd -b /bin/bash', 'useradd -s /bin/bash', 'useradd -shell /bin/bash', 'useradd -sh /bin/bash'],
    correctIndices: [1],
    explanation: 'useradd -s specifies the user\'s login shell.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-56',
    question: 'To set password expiry, use...',
    options: ['passwd -e', 'chage', 'usermod -p', 'expirepass'],
    correctIndices: [1],
    explanation: 'chage is used to change user password expiry information.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-57',
    question: 'To lock a user account, use...',
    options: ['usermod -d', 'usermod -L', 'usermod -x', 'passwd -d'],
    correctIndices: [1],
    explanation: 'usermod -L locks a user account.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-58',
    question: 'To unlock a user account, use...',
    options: ['usermod -u', 'usermod -U', 'usermod -l', 'passwd -u'],
    correctIndices: [1],
    explanation: 'usermod -U unlocks a user account.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-59',
    question: 'To disable a user\'s shell, set shell to...',
    options: ['/bin/false', '/bin/null', '/sbin/nologin', '/bin/disabled'],
    correctIndices: [2],
    explanation: '/sbin/nologin is used to disable interactive shell access.',
    difficulty: 'G',
    category: 'Shells',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-60',
    question: 'The default shell is usually...',
    options: ['/bin/sh', '/bin/bash', '/bin/zsh', '/bin/csh'],
    correctIndices: [1],
    explanation: '/bin/bash is the default shell on most Linux systems.',
    difficulty: 'G',
    category: 'Shells',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-61',
    question: '/etc/passwd fields are separated by...',
    options: [',', ';', ':', '|'],
    correctIndices: [2],
    explanation: 'Fields in /etc/passwd are separated by colons (:).',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-62',
    question: 'The 7 fields in /etc/passwd are username:password:UID:GID:...',
    options: ['home:shell:comment', 'comment:home:shell', 'shell:home:comment', 'comment:shell:home'],
    correctIndices: [1],
    explanation: 'The full format is username:password:UID:GID:comment:home:shell.',
    difficulty: 'VG',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-63',
    question: 'An x in password field means...',
    options: ['No password', 'Account disabled', 'Password in /etc/shadow', 'Root access'],
    correctIndices: [2],
    explanation: 'An x indicates the password is stored in /etc/shadow.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-64',
    question: 'The command to show password aging info is...',
    options: ['passwd -l', 'chage -l', 'usermod -l', 'showage'],
    correctIndices: [1],
    explanation: 'chage -l shows password aging information for a user.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-65',
    question: 'Primary group is set with...',
    options: ['usermod -G', 'usermod -g', 'usermod -aG', 'groupmod'],
    correctIndices: [1],
    explanation: 'usermod -g sets the primary group for a user.',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-66',
    question: 'Secondary groups are set with...',
    options: ['usermod -g', 'usermod -G', 'usermod -s', 'groupadd'],
    correctIndices: [1],
    explanation: 'usermod -G sets secondary groups (use with -a to append).',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-67',
    question: 'To delete user and home directory, use...',
    options: ['userdel -h', 'userdel -r', 'userdel -d', 'userdel -home'],
    correctIndices: [1],
    explanation: 'userdel -r removes the user and their home directory.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-68',
    question: 'The nobody user has UID...',
    options: ['0', '1', '99', '65534'],
    correctIndices: [3],
    explanation: 'The nobody user typically has UID 65534.',
    difficulty: 'VG',
    category: 'User IDs',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-69',
    question: 'System users typically have UID...',
    options: ['0', '1-999', '1000+', '65534'],
    correctIndices: [1],
    explanation: 'System users typically have UIDs in the range 1-999.',
    difficulty: 'G',
    category: 'User IDs',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-70',
    question: 'To create a system user, use...',
    options: ['useradd -s', 'useradd -r', 'useradd -sys', 'useradd -system'],
    correctIndices: [1],
    explanation: 'useradd -r creates a system user.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-71',
    question: 'Select all that are valid shells (choose 4):',
    options: ['/bin/bash', '/bin/cmd', '/bin/sh', '/bin/shell', '/bin/zsh', '/bin/terminal', '/bin/dash', '/bin/prompt', '/bin/command', '/bin/run'],
    correctIndices: [0, 2, 4, 6],
    explanation: '/bin/bash, /bin/sh, /bin/zsh, and /bin/dash are all valid shells.',
    difficulty: 'VG',
    category: 'Shells',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-72',
    question: 'The command getent passwd shows...',
    options: ['Only local users', 'All users including LDAP', 'Encrypted passwords', 'Logged in users'],
    correctIndices: [1],
    explanation: 'getent passwd shows all users including those from LDAP and other name services.',
    difficulty: 'VG',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-73',
    question: 'To change your own password, run...',
    options: ['passwd username', 'passwd', 'chpasswd', 'setpasswd'],
    correctIndices: [1],
    explanation: 'Running passwd without arguments changes your own password.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-74',
    question: 'Only root can change others\' passwords',
    options: ['True', 'False'],
    correctIndices: [0],
    explanation: 'Only root (or users with sudo) can change other users\' passwords.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-75',
    question: 'To force password change at next login, use...',
    options: ['passwd -f', 'passwd -e', 'passwd -n', 'passwd -c'],
    correctIndices: [1],
    explanation: 'passwd -e expires the password, forcing a change at next login.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-76',
    question: 'The wheel group is for...',
    options: ['Disk access', 'sudo access', 'Network access', 'Log access'],
    correctIndices: [1],
    explanation: 'The wheel group grants sudo access on RHEL/CentOS systems.',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-77',
    question: 'On Debian/Ubuntu, sudo group is called...',
    options: ['wheel', 'admin', 'sudo', 'root'],
    correctIndices: [2],
    explanation: 'On Debian/Ubuntu, the sudo group is named "sudo".',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-78',
    question: 'On RHEL/CentOS, sudo group is called...',
    options: ['wheel', 'admin', 'sudo', 'root'],
    correctIndices: [0],
    explanation: 'On RHEL/CentOS, the sudo group is named "wheel".',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-79',
    question: 'umask 022 creates files with permission...',
    options: ['755', '644', '777', '666'],
    correctIndices: [1],
    explanation: 'umask 022 creates files with 644 (666 - 022) and directories with 755.',
    difficulty: 'VG',
    category: 'Umask',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-80',
    question: 'umask 077 creates files with permission...',
    options: ['755', '644', '600', '700'],
    correctIndices: [2],
    explanation: 'umask 077 creates files with 600 (666 - 077) permissions.',
    difficulty: 'VG',
    category: 'Umask',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-81',
    question: 'Default umask for users is usually...',
    options: ['000', '077', '022', '027'],
    correctIndices: [2],
    explanation: 'The default umask is usually 022.',
    difficulty: 'G',
    category: 'Umask',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-82',
    question: 'umask subtracts from...',
    options: ['755', '644', '666 (files) / 777 (dirs)', '700'],
    correctIndices: [2],
    explanation: 'umask subtracts from 666 for files and 777 for directories.',
    difficulty: 'VG',
    category: 'Umask',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-83',
    question: 'The command to show umask is...',
    options: ['showmask', 'getmask', 'umask', 'mask'],
    correctIndices: [2],
    explanation: 'The umask command displays the current umask value.',
    difficulty: 'G',
    category: 'Umask',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-84',
    question: 'Select all user-related files (choose 3):',
    options: ['/etc/passwd', '/etc/users', '/etc/shadow', '/etc/passwords', '/etc/group', '/etc/groups', '/etc/accounts', '/etc/logins', '/etc/members', '/etc/teams'],
    correctIndices: [0, 2, 4],
    explanation: '/etc/passwd, /etc/shadow, and /etc/group are the three main user-related files.',
    difficulty: 'VG',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-85',
    question: 'To see who is logged in, use...',
    options: ['logged', 'users', 'who', 'logins'],
    correctIndices: [2],
    explanation: 'The who command shows who is currently logged in.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-86',
    question: 'To see login history, use...',
    options: ['history', 'logins', 'last', 'loginlog'],
    correctIndices: [2],
    explanation: 'The last command shows login history.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-87',
    question: 'To see failed logins, use...',
    options: ['failed', 'lastb', 'faillog', 'badlogins'],
    correctIndices: [1],
    explanation: 'The lastb command shows failed login attempts.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-88',
    question: 'The command w shows...',
    options: ['Current directory', 'Who is logged in and what they\'re doing', 'Wrong logins', 'Warnings'],
    correctIndices: [1],
    explanation: 'The w command shows who is logged in and what they are doing.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-89',
    question: 'newgrp command...',
    options: ['Creates new group', 'Changes current group temporarily', 'Shows groups', 'Deletes group'],
    correctIndices: [1],
    explanation: 'newgrp changes the current group temporarily for the session.',
    difficulty: 'VG',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-90',
    question: 'The sg command...',
    options: ['Shows groups', 'Runs command as different group', 'Sets group', 'System group'],
    correctIndices: [1],
    explanation: 'sg runs a command with a different group ID.',
    difficulty: 'VG',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-91',
    question: 'ACL stands for...',
    options: ['Account Control List', 'Access Control List', 'Admin Control Level', 'Access Command List'],
    correctIndices: [1],
    explanation: 'ACL stands for Access Control List.',
    difficulty: 'G',
    category: 'ACL',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-92',
    question: 'To view ACL, use...',
    options: ['showacl', 'lsacl', 'getfacl', 'acl'],
    correctIndices: [2],
    explanation: 'getfacl displays the Access Control List for a file.',
    difficulty: 'G',
    category: 'ACL',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-93',
    question: 'To set ACL, use...',
    options: ['addacl', 'chacl', 'setfacl', 'acl'],
    correctIndices: [2],
    explanation: 'setfacl is used to set Access Control Lists.',
    difficulty: 'G',
    category: 'ACL',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-94',
    question: '/etc/skel contains...',
    options: ['Skeleton keys', 'Template for new user homes', 'System skeletons', 'Deleted users'],
    correctIndices: [1],
    explanation: '/etc/skel contains template files copied to new user home directories.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-95',
    question: 'Files in /etc/skel are copied when...',
    options: ['User logs in', 'User is created with -m', 'System boots', 'User changes password'],
    correctIndices: [1],
    explanation: 'Files from /etc/skel are copied when a user is created with -m flag.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-96',
    question: 'Select all valid usermod flags (choose 4):',
    options: ['-aG', '-add', '-L', '-lock', '-s', '-shell', '-d', '-dir', '-home', '-user'],
    correctIndices: [0, 2, 4, 6],
    explanation: '-aG (append group), -L (lock), -s (shell), and -d (home directory) are valid usermod flags.',
    difficulty: 'VG',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-97',
    question: 'To change username, use...',
    options: ['usermod -n', 'usermod -l', 'usermod -u', 'usermod -name'],
    correctIndices: [1],
    explanation: 'usermod -l changes the username (login name).',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-98',
    question: 'To change user\'s UID, use...',
    options: ['usermod -i', 'usermod -u', 'usermod -uid', 'usermod -id'],
    correctIndices: [1],
    explanation: 'usermod -u changes the user\'s UID.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-99',
    question: 'To add comment/description, use...',
    options: ['usermod -d', 'usermod -c', 'usermod -comment', 'usermod -desc'],
    correctIndices: [1],
    explanation: 'usermod -c adds or changes the comment field (GECOS).',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-100',
    question: 'The finger command shows...',
    options: ['File info', 'User info', 'Fingerprint', 'Touch info'],
    correctIndices: [1],
    explanation: 'The finger command displays user information.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-101',
    question: 'passwd -S shows...',
    options: ['Set password', 'Password status', 'Shadow info', 'System password'],
    correctIndices: [1],
    explanation: 'passwd -S shows the password status for a user.',
    difficulty: 'G',
    category: 'Password Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-102',
    question: 'A locked account shows...',
    options: ['! in /etc/passwd', '! or !! in /etc/shadow', 'L in /etc/passwd', 'LOCKED in shadow'],
    correctIndices: [1],
    explanation: 'A locked account has ! or !! prefixed to the password hash in /etc/shadow.',
    difficulty: 'VG',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-103',
    question: 'The nologin message is in...',
    options: ['/etc/nologin.msg', '/etc/nologin.txt', '/etc/message', '/var/nologin'],
    correctIndices: [1],
    explanation: 'The nologin message is stored in /etc/nologin.txt.',
    difficulty: 'VG',
    category: 'User Files',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-104',
    question: 'To expire account on date, use...',
    options: ['usermod -d', 'usermod -e YYYY-MM-DD', 'chage -d', 'passwd -e'],
    correctIndices: [1],
    explanation: 'usermod -e sets the account expiration date.',
    difficulty: 'G',
    category: 'User Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-105',
    question: 'GID 0 is for group...',
    options: ['users', 'wheel', 'root', 'admin'],
    correctIndices: [2],
    explanation: 'GID 0 is reserved for the root group.',
    difficulty: 'G',
    category: 'Group Commands',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-106',
    question: 'Select all ways to become root (choose 3):',
    options: ['sudo -i', 'root', 'su -', 'admin', 'sudo su', 'superuser', 'become root', 'switch root', 'login root', 'enter root'],
    correctIndices: [0, 2, 4],
    explanation: 'sudo -i, su -, and sudo su are valid ways to become root.',
    difficulty: 'VG',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-107',
    question: 'su - vs su difference...',
    options: ['No difference', 'su - loads root\'s environment', 'su - is faster', 'su is deprecated'],
    correctIndices: [1],
    explanation: 'su - loads root\'s environment (login shell), while su keeps the current environment.',
    difficulty: 'VG',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-108',
    question: 'sudo -i does...',
    options: ['Shows info', 'Starts root shell with environment', 'Installs package', 'Shows identity'],
    correctIndices: [1],
    explanation: 'sudo -i starts an interactive root shell with root\'s environment.',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-109',
    question: 'To run single command as root...',
    options: ['root command', 'sudo command', 'su command', 'admin command'],
    correctIndices: [1],
    explanation: 'sudo command runs a single command with root privileges.',
    difficulty: 'G',
    category: 'Sudo',
    topic: 'anvandarhantering'
  },
  {
    id: 'omtenta-v2-user-110',
    question: '/etc/login.defs contains...',
    options: ['Login messages', 'Default user settings', 'Login scripts', 'Login logs'],
    correctIndices: [1],
    explanation: '/etc/login.defs contains default settings for user account creation.',
    difficulty: 'G',
    category: 'User Files',
    topic: 'anvandarhantering'
  }
]
