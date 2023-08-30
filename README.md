## Rank Maximal Matching Algorithm
Algorithm Demo: A Simple Flask Web App

### Requirements:
python3, pip , virtualenv, google credentials

### Installation:

1. Clone the repository:
   ```
   git clone https://github.com/oriyalperin/rmm_flask_app
   ```

2. Change directory to the cloned repository:
   ```
   cd rmm_flask_app
   ```

3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

5. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

6. Add the `google-credentials.json` file:

   Run the following command:
   ```
   nano google-credentials.json
   ```
   Then, paste your credentials into this file.
   

8. Run the app using:
   ```
   python run.py
   ```

9. You can access the app at:
   ```
   http://localhost:2704
   ```

[comment]: <> (The web app can be accessed at )
### Learn more about the algorithm :
* [Article](https://d1wqtxts1xzle7.cloudfront.net/43890109/Rank-maximal_matchings20160319-5330-17us31z-libre.pdf?1458398152=&response-content-disposition=inline%3B+filename%3DRank_maximal_matchings.pdf&Expires=1673263482&Signature=QWSV3VJZC2I8dPn9D5m~yNr3gHECtLyuRwMTPc9QxVBI5VdQ579hR-~wwF5bprXiCSolrHbsKAzrwTb3OG-lswHm42eLMnWvAUgyKzxVc7V9FTR2expMXWm-5Eaz7nnh-Q1TbaKSm42B0ujvTI5pIkUXYqJohvehO~VFlQHSIPT68IHjX8fNUaPhI5K00xGtCIemxP~eV5Mm-Vh1aTr9uCiGHWRd-jG1qGHfNtI1Kfy33rhqKal0jhvAy2KbuxsGXpWxhmzlVtpttqCDbvRj-9ogzaCB-y0XwSrPa5uSsbZ0bsKsPlpPe7nUnmxYXii5yOXiIcdicZ~o~Z8WZRSOuQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
* [Implementation](https://github.com/OLAnetworkx/networkx/blob/rank-maximal-matching/networkx/algorithms/bipartite/rank_maximal_matching.py)
