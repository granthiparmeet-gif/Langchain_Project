export MAMBA_ROOT_PREFIX="/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER"
__mamba_setup="$("/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER/bin/mamba" shell hook --shell posix 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER/bin/mamba"  # Fallback on help from mamba activate
fi
unset __mamba_setup
