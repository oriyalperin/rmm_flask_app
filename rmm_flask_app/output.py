import gspread
import networkx as nx
import matplotlib.pyplot as plt
import uuid


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
    plt.savefig(f"static/media/{graph_name}.png")
    nx.draw_networkx_edges(G, pos=pos, edgelist=matching_edges, edge_color='#FF0000', width=3)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)
    matching_name = uuid.uuid4().hex[:6].upper()
    plt.savefig(f"static/media/{matching_name}.png")
    return {"graph": graph_name, "matching": matching_name}

def make_output_animation(G, matching_edges, matching_edge_labels, edge_labels, rater_list, callback=None):
    import matplotlib.animation as animation
    pos = nx.bipartite_layout(G, nodes=rater_list)
    fig, ax = plt.subplots(figsize=(10, 10))
    matching_graph = nx.Graph()
    matching_graph.add_edges_from(matching_edge_labels)
    nx.draw(G, pos=pos, with_labels=True, node_color='#999FFF', node_size=500, edge_color='#999999', width=6)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)

    nx.draw_networkx_edges(G, pos=pos, edgelist=matching_edges, edge_color='#FF0000', width=5)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)




    def update(i):
        if i % 3 == 0:
            plt.clf()
            nx.draw(G, pos=pos, with_labels=True, node_color='#999FFF', node_size=500, edge_color='#999999', width=6)
            nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)
            pass
        elif i % 3 == 1:
            nx.draw_networkx_edges(G, pos=pos, edgelist=matching_edges, edge_color='#FF0000', width=5)
            nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.2)
        else:
            plt.clf()
            nx.draw(matching_graph, pos=pos, with_labels=True, node_color='#999FFF', node_size=500,
                    edge_color='#FF0000', width=5)
            nx.draw_networkx_edge_labels(matching_graph, pos=pos, edge_labels=matching_edge_labels, label_pos=0.2)
        for label in plt.gca().get_yticklabels():
            label.set_verticalalignment('bottom')
            label.set_y(-5)

    #ani = animation.FuncAnimation(fig, update, frames=range(10), interval=1000)
    #ani.save('static/media/animation.gif', writer='imagemagick')
