import networkx as nx
from rmm_flask_app.rmm_algo import rank_maximal_matching
import rmm_flask_app.output as output
import gspread
import numpy as np


def run(url: str):
    account = gspread.service_account("credentials.json")
    # Open spreadsheet by name:
    spreadsheet = account.open_by_url(url)
    # Open sheet by name:
    input_sheet = spreadsheet.worksheet("input")

    rater_list = []
    edge_labels = {}
    G = nx.Graph()
    records = input_sheet.get_all_records()
    for record in records:
        rater_name = record.pop('agent/item')
        rater_list.append(rater_name)
        for rated_name, rating in record.items():
            if rating != '' and type(rating) == int and rating >= 0:
                G.add_edge(rater_name, rated_name, rank=rating)
                edge_labels[(rater_name, rated_name)] = rating
    matching = rank_maximal_matching(G, top_nodes=rater_list, rank="rank")
    output_sheet = output.worksheet(spreadsheet, len(matching) / 2, 3)
    output_sheet.clear()
    output_lst = [["agent", "item", "rank"]]

    matching_edge_labels = {}
    for i, (rater, rated) in enumerate(matching.items()):
        print(rater, rated)
        if i == len(matching) / 2:
            break
        rating = G[rater][rated]["rank"]
        matching_edge_labels[(rater, rated)] = rating
        output_lst.append([rater, rated, rating])

    output_sheet.update('A1', np.array(output_lst).tolist())
    output_sheet.format("A1:C1", {
        "backgroundColor": {
            "red": 20.0,
            "green": 20.0,
            "blue": 20.0
        }})
    matching_edges = [tuple(edge) for edge in matching.items()]

    from multiprocessing import Pool
    with Pool(1) as p:
        return p.apply(output.create_output_images,
                       args=(G, matching_edges, matching_edge_labels, edge_labels, rater_list))
