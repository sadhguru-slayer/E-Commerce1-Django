o
    �dt  �                   @   s6   d dl mZmZ d dlZd dlZG dd� dej�ZdS )�    )�
migrations�modelsNc                   @   s�   e Zd ZdgZejddejdej	jj
jdd�d�ejddejejjjd	�d�ejdd
ejdej	jj
jdd�d�ejddejddddd�d�ejddejddgddd�d�ejddejdej	jj
jdd�d�gZdS )�	Migration)�EcommerceappZ0010_product_type�products�Price_Filter� zEcommerceapp.price_filter)�default�	on_delete�to)�
model_name�name�field�created_date)r	   �product_brandzEcommerceapp.brands�
product_idT�d   )�blank�
max_length�null�unique�stock)�IN STOCKr   )�OUT OF STOCKr   )�choicesr	   r   �product_categoryzEcommerceapp.categoriesN)�__name__�
__module__�__qualname__�dependenciesr   �AddFieldr   �
ForeignKey�django�db�deletion�CASCADE�DateTimeField�utils�timezone�now�	CharField�
AlterField�
operations� r-   r-   ��C:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0011_products_price_filter_products_created_date_and_more.pyr      sD    ��������r   )�	django.dbr   r   �django.db.models.deletionr"   �django.utils.timezoner   r-   r-   r-   r.   �<module>   s   