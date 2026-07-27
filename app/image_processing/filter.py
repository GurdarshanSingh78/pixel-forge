def filter_images(image_paths, query, num_results=None, **kwargs):
    """
    Bypass the heavy PyTorch AI filtering to save memory on Render.
    Simply returns the requested number of downloaded images.
    """
    print(f"Bypassing AI filter for query '{query}'. Returning up to {len(image_paths)} images.")
    
    if num_results:
        return image_paths[:num_results]
    return image_paths