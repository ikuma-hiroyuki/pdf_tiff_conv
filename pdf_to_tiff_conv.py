import os
import glob
from pathlib import Path
from pdf2image import convert_from_path


# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler-0.68.0/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

target_dir = input("Input the target folder.\n")
image_dir = input("Input Moving destination Folder.\n") + "/"


def pdf_to_tiff(file_path: str):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    is_exist = os.path.exists("./image_file/" + file_name + ".tif")

    if is_exist is False:
        print(f"Start {file_name}")
        pdf_path = Path(file_path)
        pages = convert_from_path(
            pdf_path=str(pdf_path),
            dpi=150,
            grayscale=True)

        # image_dir = Path("./image_file")
        tiff_name = pdf_path.stem + ".tif"
        image_path = Path(image_dir) / tiff_name
        pages[0].save(
            str(image_path),
            compression="tiff_deflate",
            save_all=False,
            first_page=1,
            last_page=1,
            thread_count=1)
        print(f"Conversion complete {file_name}.pdf")
    else:
        print(f"{file_name}.tif is exist.")


if target_dir != "" or image_dir != "":
    files = glob.glob(target_dir + "/*")
    for file in files:
        pdf_to_tiff(file)
