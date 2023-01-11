from flask import render_template, request
from rmm_flask_app import app

import gspread

account = gspread.service_account("google-credentials.json")


@app.route('/')
def root():
    return render_template('data.html')


@app.route('/get_data_from_gspread')
def get_data_from_gspread():
    url = request.args.get('url')
    print("url=", url)
    error = None
    try:
        print("account=", account)
        spreadsheet = account.open_by_url(url)
        print("spreadsheet=", spreadsheet)
    except gspread.exceptions.APIError:
        error = "Google Spreadsheet API error, please verify you shared your spreadsheet with the above address"
    except gspread.exceptions.NoValidUrlKeyFound:
        error = "Google Spreadsheet could not find a key in your URL,please check that the URL you entered points to " \
                "a valid spreadsheet "
    except gspread.exceptions.SpreadsheetNotFound:
        error = "Google Spreadsheet could not find the spreadsheet you entered, please check your URL points to a " \
                "valid spreadsheet "
    except Exception as e:
        error = type(e).__name__ + ", please check your URL and try again"
    if error is not None:
        print("error=", error)
        return render_template("data.html", error=error)
    else:
        return render_template("data_view.html", url=url)


@app.route('/run_the_algorithm')
def run_the_algorithm():
    url = request.args.get('url')
    import run
    names = run.run(url=url)
    return names

