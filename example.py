'''
alias = Alias([
    Generic("{}", DataTypes.IMAGE_NAME),
    Generic("{}_{}", DataTypes.CLASS_NAME, DataTypes.GENERIC)
])
root = '/Users/atong/Documents/Datasets/OxfordPets'
form = {
    Static("annotations"): {
        Generic("{}.txt", DataTypes.IMAGE_SET): TXTFile(
            Generic(
                "{} {} {} {}", alias, DataTypes.GENERIC, DataTypes.GENERIC, DataTypes.CLASS_ID
            ),
            ignore_type = '#'
        )
    },
    Static("images"): {
        Generic("{}.jpg", alias): Image()
    },
    Static("class.txt"): TXTFile(
        Generic("{} {}", DataTypes.CLASS_NAME, DataTypes.CLASS_ID)
    )
}
dataset = Dataset(root, form)
'''

from src import *

if __name__ == '__main__':
    form = {
        'temp.json': JSONFile({
            'images': GenericList([{
                'id': DataTypes.IMAGE_ID,
                'file_name': DataTypes.IMAGE_NAME
            }]),
            'categories': GenericList([{
                'id': DataTypes.CLASS_ID,
                'name': DataTypes.CLASS_NAME
            }]),
            'annotations': GenericList([{
                'image_id': DataTypes.IMAGE_ID,
                'category_id': DataTypes.CLASS_ID,
                'bbox': GenericList([
                    DataTypes.XMIN, DataTypes.YMIN, DataTypes.XMAX, DataTypes.YMAX
                ])
            }])
        })
    }
    dataset = Dataset('/Users/atong/Documents/Datasets/Avo', form)
