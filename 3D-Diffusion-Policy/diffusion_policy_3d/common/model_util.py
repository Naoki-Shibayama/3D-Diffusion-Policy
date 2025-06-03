

def print_params(model):
    """
    Print the number of parameters in each part of the model.
    """    
    params_dict = {}

    all_num_param = sum(p.numel() for p in model.parameters())

    for name, param in model.named_parameters():
        part_name = name.split('.')[0]
        if part_name not in params_dict:
            params_dict[part_name] = 0
        params_dict[part_name] += param.numel()

    print(f'----------------------------------')
    print(f'Class name: {model.__class__.__name__}')
    print(f'  Number of parameters: {all_num_param / 1e6:.4f}M')
    for part_name, num_params in params_dict.items():
        print(f'   {part_name}: {num_params / 1e6:.4f}M ({num_params / all_num_param:.2%})')
    print(f'----------------------------------')