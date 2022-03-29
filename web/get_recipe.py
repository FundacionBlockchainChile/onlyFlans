from get_module import get_info

def get_recipe(name):
  """
#     [Retorna lista de recetas]
#     Args:
#         name (str): [palabra a buscar]         
#     Returns:
#         [List]: [Retorna lista de recetas] 
# """
  try:
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={name}&apiKey=c9124529c27b47568032526837fe0f8b'
    recipes_dictionary = get_info(url)
    return recipes_dictionary['results']
  except:
    return []

if __name__ == '__main__':
  listaRecetas  = get_recipe('flan')
  print(listaRecetas)