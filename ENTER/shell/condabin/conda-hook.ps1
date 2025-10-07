$Env:CONDA_EXE = "/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER/bin/conda"
$Env:_CONDA_EXE = "/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER/bin/conda"
$Env:_CE_M = $null
$Env:_CE_CONDA = $null
$Env:CONDA_PYTHON_EXE = "/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER/bin/python"
$Env:_CONDA_ROOT = "/Users/parmeetsingh/Desktop/Langchain- Projects/ENTER"
$CondaModuleArgs = @{ChangePs1 = $True}

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs