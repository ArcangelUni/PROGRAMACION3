digraph G {
  
    subgraph cluster_0 {
      node [style=filled];
      Null_Inicio -> a1 -> a0 -> a2 -> Null_Final
      Null_Final -> a2 -> a0 -> a1 -> Null_Inicio
      a2 [fillcolor=red]
      label = "Eliminar Inicio";
      color=blue
    }

    subgraph cluster_1 {
        style=filled;
        color=lightgrey;
        node [style=filled,color=white];
        Null_Inicio_ -> a1_ -> a0_ -> Null_Final_
        Null_Final_ -> a0_ -> a1_ -> Null_Inicio_
        label = "Eliminar Inicio";
      }
  }