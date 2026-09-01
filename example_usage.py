from client import ProceduralAstFlowchartLogicDiagramSynthesizerClient

def main():
    client = ProceduralAstFlowchartLogicDiagramSynthesizerClient()
    res = client.synthesize_flowchart('OAuth 2.0 PKCE authentication handshake workflow')
    print('Flowchart Synthesizer: ' + res['flowchart_id'] + ' (Decision Nodes: ' + str(res['decision_diamonds_count']) + ')')
    print('Syntax Validated: ' + str(res['syntax_graph_validated']))
    print('Mermaid:\n' + res['mermaid_diagram_definition'])
    print('SVG URL: ' + res['rendered_svg_diagram_url'])

if __name__ == '__main__':
    main()
