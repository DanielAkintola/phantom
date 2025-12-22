from featureExtractor import featureExtraction
from pycaret.classification import load_model, predict_model
import typer

app = typer.Typer()

model = load_model('model/phishingdetection')


def predict(url):
    data = featureExtraction(url)
    result = predict_model(model, data=data)
    
    # Get the prediction score for the positive class (Phishing)
    prediction_score = result['prediction_score'][0]  
    prediction_label = result['prediction_label'][0]  
    # domain_age = result['Domain_Age'][0]  
    # print('Result -> ', url)
    
    return {
        'prediction_label': prediction_label,
        'prediction_score': prediction_score * 100,
    }


def show_banner():
    banner = """
==================================================
  ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗
  ██╔══██╗██║  ██║██╔══██╗████╗  ██║
  ██████╔╝███████║███████║██╔██╗ ██║
  ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║
  ██║     ██║  ██║██║  ██║██║ ╚████║
  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
==================================================
        Phishing Detection Engine (PHANTOM)
==================================================
"""
    print(banner)

def get_url():
    print("\n")
    url = input("Enter URL: ").strip()
    return url



@app.command()
def check_url():
    show_banner()
    user_input = get_url()
    result = predict(user_input)

    show_result(user_input, result)


def show_result(url: str, result: dict):
    score = result["prediction_score"]
    label = result["prediction_label"]

    typer.echo("\n========================================")

    typer.echo(
        typer.style("URL: ", fg=typer.colors.CYAN) + url
    )

    typer.echo(
        typer.style("Confidence: ", fg=typer.colors.YELLOW)
        + f"{score:.2f}%"
    )

    if label == 1:
        typer.echo(
            typer.style("\n[!] PHISHING DETECTED", fg=typer.colors.RED, bold=True)
        )
        typer.echo(
            typer.style("Status: INSECURE", fg=typer.colors.RED, bold=True)
        )
    else:
        typer.echo(
            typer.style("\n[✓] URL APPEARS SAFE", fg=typer.colors.GREEN, bold=True)
        )
        typer.echo(
            typer.style("Status: SECURE", fg=typer.colors.GREEN, bold=True)
        )

    typer.echo("========================================\n")



@app.command()
def check_urls():
    print("hello")
   
if __name__ == "__main__":
    app()
