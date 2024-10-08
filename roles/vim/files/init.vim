" Ansible managed

call plug#begin(stdpath('data') . '/plugged')

Plug 'itchyny/lightline.vim'
let g:lightline = {'colorscheme': 'solarized'}

Plug 'dense-analysis/ale'

Plug 'airblade/vim-gitgutter'
set updatetime=10

call plug#end()

" Show trailing whitespace
set list
set listchars=trail:·

" Disable swap files
set noswapfile

" Style
set number
set cursorline

" Mouse
set mouse=a

" Copying
set clipboard+=unnamedplus

" Replace tabs with spaces
set expandtab
set tabstop=4
set shiftwidth=4

" Spell checking
set spelllang=en,nl
set spell
nnoremap <F7> :setlocal spell! <CR>

" Clear highlighting till the next search
nnoremap <C-L> :nohl<CR><C-L>

set guicursor=
