
MATERIAL_NAMES = [
    "Plain Red",
    "Plain Blue",
    "Plain Green",
    "Plain Yellow"
]

MATERIAL_COLORS = [
    (200,0,0),
    (0,0,200),
    (0,200,0),
    (200,200,0)
]

all_material_names = []
materials = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()

t = Transaction(doc)
t.Start("Create Material")

def get_existed_mat(name):
    for mat in materials:
        if mat.Name == name:
            return (mat.Id)
    return Material.Create(doc, name)

for name, color in zip(MATERIAL_NAMES, MATERIAL_COLORS):
    new_matId = get_existed_mat(name)
    new_mat = doc.GetElement(new_matId)
    new_mat.Color = Color(color[0], color[1], color[2])

t.Commit()