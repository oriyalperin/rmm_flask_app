import gspread
import networkx as nx
import matplotlib.pyplot as plt
import uuid
import io

def worksheet(spreadsheet: gspread.Spreadsheet, new_row_count, new_col_count) -> gspread.Worksheet:
    try:
        output_sheet = spreadsheet.worksheet("output")
    except gspread.exceptions.WorksheetNotFound:
        output_sheet = spreadsheet.add_worksheet(title="output", rows=new_row_count, cols=new_col_count)
    if output_sheet.row_count < new_row_count:
        output_sheet.add_rows(new_row_count - output_sheet.row_count)
    if output_sheet.col_count < new_col_count:
        output_sheet.add_cols(new_col_count - output_sheet.col_count)
    return output_sheet


def create_output_images(G, matching_edges, matching_edge_labels, edge_labels, rater_list):
    pos = nx.bipartite_layout(G, nodes=rater_list)
    matching_graph = nx.Graph()
    matching_graph.add_edges_from(matching_edge_labels)
    nx.draw(G, pos=pos, with_labels=True, node_color='#999FFF', node_size=500, edge_color='#999999', width=4)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)
    graph_name = uuid.uuid4().hex[:6].upper()
    buf_graph = io.BytesIO()
    plt.savefig(buf_graph,format='png')
# Seek to the beginning of the BytesIO object
    buf_graph.seek(0)
    nx.draw_networkx_edges(G, pos=pos, edgelist=matching_edges, edge_color='#FF0000', width=3)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)
    matching_name = uuid.uuid4().hex[:6].upper()
    buf_match = io.BytesIO()
    plt.savefig(buf_match, format='png')
    # Seek to the beginning of the BytesIO object
    buf_match.seek(0)
    plt.clf()
    return {"graph": {"name": graph_name, "img":buf_graph}, "matching": {"name":matching_name,"img":buf_match}}
