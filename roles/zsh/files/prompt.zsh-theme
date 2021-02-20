local time='%{$fg[red]%}%D{%H:%M:%S}%{$reset_color%}'

local user='%{$fg[magenta]%}%n@%{$fg[magenta]%}%m%{$reset_color%}'
local user_remote='%{$fg_bold[green]%}%n@%{$fg_bold[green]%}%m%{$reset_color%}'

local pwd='%{$fg[blue]%}%~%{$reset_color%}'

local return_code='%(?..%{$fg[red]%}%? ↵%{$reset_color%})'
local git_branch='$(git_prompt_status)%{$reset_color%}$(git_prompt_info)%{$reset_color%}'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[green]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"

ZSH_THEME_GIT_PROMPT_ADDED="%{$fg[green]%} ✚"
ZSH_THEME_GIT_PROMPT_MODIFIED="%{$fg[blue]%} ✹"
ZSH_THEME_GIT_PROMPT_DELETED="%{$fg[red]%} ✖"
ZSH_THEME_GIT_PROMPT_RENAMED="%{$fg[magenta]%} ➜"
ZSH_THEME_GIT_PROMPT_UNMERGED="%{$fg[yellow]%} ═"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg[cyan]%} ✭"

if [[ -n $SSH_CONNECTION ]]; then
    PROMPT="${time} ${user_remote} ${pwd}$ "
else
    PROMPT="${time} ${user} ${pwd}$ "
fi

RPROMPT="${return_code} ${git_branch}"
