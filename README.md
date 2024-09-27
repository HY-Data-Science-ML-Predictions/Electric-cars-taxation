# Electric-cars-taxation

[Mini project canvas](https://intro-to-ds.slack.com/archives/C07KZ8XTAUD/p1726061687818359)


[Data source from the Statistics Finland](https://intro-to-ds.slack.com/archives/C07KZ8XTAUD/p1725533179688559)

# Install venv and dependencies

1) Install virtual environment (Ubuntu) with `python3 -m venv intro_to_ds_env`.
2) Activate virtual environment `source intro_to_ds_env/bin/activate`
3) Install dependencies from `requirements.txt` with pip (or some another package manager) `pip install -r requirements.txt`

# Run Jupyter Notebook

## Vscode

If you use Visual Studio Code then simplest way to install and use Jupyter Notebook is to install the Jupyter Notebook extension `Jupyter`. Then select virtual environment `intro_to_ds_env` as kernel.

## Local Server

To run Jupyter Notebook locally you can simply start the server `jupyter notebook`.

You might need to add the kernel to the server as follows `python3 -m ipykernel install --user --name=intro_to_ds_env --display-name "Python (intro_to_ds_env)"`