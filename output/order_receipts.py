from robocorp.tasks import task
from robocorp.browser import browser

from RPA.HTTP import HTTP
from RPA.Tables import Tables
from RPA.PDF import PDF
import shutil
from pathlib import Path
@task
def order_robots_from_RobotSpareBin():
        
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """

def open_robot_order_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")
    order_robot_from_webite()

    def order_robot_from_webite():
        """Download the orders file, read it as a table, and return the result"""

        http = HTTP
        http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)

def read_data_from_order_file():
        """read_order_file_as_table and returns the result"""
        library = Tables()
        orders = library.read_table_from_csv(
        "orders.csv", columns=["name", "mail", "product"]
        )

        customers = library.group_table_by_column(rows, "mail")
        rows="[Order number,Head,Body,Legs,Address]"

        return_value = orders("get_orders")

        print(return_value)

        for rows in "<collection>":
            "<Order number,Head,Body,Legs,Address>"

def close_annoying_modal():
        """Gets rid of that annoying modal that pops up when you open the robot order website"""
        page = browser.page() 
        page.click("button:text('Ok')")

def fill_order_form():
        page = browser.page
        page.fill("row['#Order number']")
        page.fill("row['#Head']")
        page.fill("row['#Body']")
        page.select_option("row['#Legs', str(Legs)]")
        page.fill("row['#Address']")
        page.click("button:text('Preview)")
        page.click("button:text('Order')")
        if "<expr>": False
        "<statement>" 
        page.click("button:text('Order')")

def screenshot_robot(order_number):
    """Saves a screenshot of the ordered robot"""
    page = browser.page()
    page.screenshot(path="output/order_receipts.png")

def store_receipt_as_pdf(order_number):
    """Saves the order HTML receipt as a PDF file"""
    page = browser.page()
    order_receipt_html = page.locator("#order-receipt").inner_html()

    pdf = PDF()
    pdf.html_to_pdf(order_receipt_html, "output/order_receipts.pdf")

def embed_screenshot_to_receipt(screenshot, pdf_file):
    """Embeds the screenshot of the robot to the PDF receipt"""
    pdf = PDF()
    pdf.add_watermark_image_to_pdf(image_path=screenshot, output_path=pdf_file)
    embed_screenshot_to_receipt("path/to/screenshot.png", "path/to/target_order_receipts.pdf")

def append_screenshot_to_pdf():
     pdf = PDF()
     list_of_files = [
        'your_existing_pdf_file.pdf',
        'your_screenshot_image.png:align=center'
     ]
     pdf.add_files_to_pdf(
        files=list_of_files,
        target_document="output/combined_document.pdf",
        append=True
     )

def order_another_robot():
    """Goes to order another robot"""
    page = browser.page()
    page.click("button:text('ORDER_ANOTHER_ROBOT')")

def archive_receipts():
    directory_to_zip = Path("path/to/order_receipts/directory")
    output_zip_path = Path("path/to/order_receipts/output_zip_file")
    shutil.make_archive(output_zip_path, 'zip', directory_to_zip)
    print(f"Created ZIP archive at: {output_zip_path}.zip")