## Rank Maximal Matching Algorithm
Algorithm Demo: A Simple Flask Web App

The web app can be accessed at https://rmm.csariel.xyz.

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
   

7. Run the app using:
   ```
   python run.py
   ```

8. You can access the app at:
   ```
   http://localhost:2704
   ```

9. You can change the port by editing the `run.py` file:
    
    Open the file with:
   ```
   sudo nano run.py
   ```
   In the main function, modify the port here:
   ```
   app.run(debug=True, host="0.0.0.0", port=<your-port>)
   ```
   Replace `<your-port>` with your chosen port number.

### Learn more about the algorithm :
* [Article](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=45a1d050f6bd63de2664c3984967b82237f206ee)
* [Implementation](https://github.com/OLAnetworkx/networkx/blob/rank-maximal-matching/networkx/algorithms/bipartite/rank_maximal_matching.py)
