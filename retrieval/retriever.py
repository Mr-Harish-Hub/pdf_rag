def retrieve_dynamic_chunks(
    query_embedding,
    index,
    chunks,
    max_k=10,
    distance_threshold=1.2
):

    distances, indices = index.search(query_embedding, max_k)

    results = []
    for i, idx in enumerate(indices[0]):
        dist = float(distances[0][i])

        if dist <= distance_threshold:
            results.append({
                "rank": len(results) + 1,
                "chunk": chunks[idx],
                "distance": dist
            })
            
    if not results:
        idx = indices[0][0]
        results.append({
            "rank": 1,
            "chunk": chunks[idx],
            "distance": float(distances[0][0])
        })

    return results
