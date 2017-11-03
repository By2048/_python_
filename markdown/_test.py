import markdown
import re,os

txt='''
属性	值	描述
accept	mime_type	规定通过文件上传来提交的文件的类型。
align	left right top middle bottom	不赞成使用。规定图像输入的对齐方式。
alt	text	定义图像输入的替代文本。
autocomplete	on off	规定是否使用输入字段的自动完成功能。
autofocus	autofocus	规定输入字段在页面加载时是否获得焦点。（不适用于 type="hidden"）
checked	checked	规定此 input 元素首次加载时应当被选中。
disabled	disabled	当 input 元素加载时禁用此元素。
form	formname	规定输入字段所属的一个或多个表单。
formaction	URL	覆盖表单的 action 属性。（适用于 type="submit" 和 type="image"）
formenctype	见注释	覆盖表单的 enctype 属性。（适用于 type="submit" 和 type="image"）
formmethod	get post	覆盖表单的 method 属性。（适用于 type="submit" 和 type="image"）
formnovalidate	formnovalidate	覆盖表单的 novalidate 属性。如果使用该属性，则提交表单时不进行验证。
formtarget	_blank _self _parent _top framename	覆盖表单的 target 属性。（适用于 type="submit" 和 type="image"）
height	pixels %	定义 input 字段的高度。（适用于 type="image"）
list	datalist-id	引用包含输入字段的预定义选项的 datalist 。
max	number date	规定输入字段的最大值。请与 "min" 属性配合使用，来创建合法值的范围。
maxlength	number	规定输入字段中的字符的最大长度。
min	number date	规定输入字段的最小值。请与 "max" 属性配合使用，来创建合法值的范围。
multiple	multiple	如果使用该属性，则允许一个以上的值。
name	field_name	定义 input 元素的名称。
pattern	regexp_pattern	规定输入字段的值的模式或格式。例如 pattern="[0-9]" 表示输入值必须是 0 与 9 之间的数字。
placeholder	text	规定帮助用户填写输入字段的提示。
readonly	readonly	规定输入字段为只读。
required	required	指示输入字段的值是必需的。
size	number_of_char	定义输入字段的宽度。
src	URL	定义以提交按钮形式显示的图像的 URL。
step	number	规定输入字的的合法数字间隔。
type	button checkbox file hidden image password radio reset submit text	规定 input 元素的类型。
value	value	规定 input 元素的值。
width	pixels %	定义 input 字段的宽度。（适用于 type="image"）
'''

txt=txt.replace('\t','    ')


lines=[]
desktop_file_path = r'E:\Desktop\table_to_md.txt'
file_size = os.path.getsize(desktop_file_path)
print(file_size)
with open(desktop_file_path, 'r') as file:
    lines=file.readlines()
    print(lines)

print("".join(lines))