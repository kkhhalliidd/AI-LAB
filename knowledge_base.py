import networkx as nx
import matplotlib.pyplot as plt

def forward_chain_with_graph():
    facts = {
        "American(Robert)",
        "Missile(T1)",
        "Owns(A, T1)",
        "Enemy(A, America)"
    }

    rules = [
        (["Missile(T1)"], "Weapon(T1)"),
        (["Missile(T1)", "Owns(A, T1)"], "Sells(Robert, T1, A)"),
        (["Enemy(A, America)"], "Hostile(A)"),
        (["American(Robert)", "Weapon(T1)", "Sells(Robert, T1, A)", "Hostile(A)"], "Criminal(Robert)")
    ]

    G = nx.DiGraph()
    for f in facts:
        G.add_node(f)

    derived = set()
    new = True

    print(" Forward Chaining Steps:\n")
    while new:
        new = False
        for premises, conclusion in rules:
            if all(p in facts for p in premises) and conclusion not in facts:
                facts.add(conclusion)
                derived.add(conclusion)
                new = True
                print(f"Inferred: {conclusion}  ←  from {', '.join(premises)}")

                
                for p in premises:
                    G.add_edge(p, conclusion)

                
                if conclusion == "Criminal(Robert)":
                    print("\n Goal Reached: Criminal(Robert)\n")
                    draw_graph(G)
                    return

    print("\n Could not prove the goal.")
    draw_graph(G)


def draw_graph(G):
    plt.figure(figsize=(9,6))
    pos = nx.spring_layout(G, k=1.2, seed=5)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2600, font_size=9, font_weight="bold", arrowsize=20)
    plt.title("Forward Chaining Graph: Crime Example", fontsize=13, fontweight="bold")
    plt.show()


# --- Run ---
forward_chain_with_graph()
