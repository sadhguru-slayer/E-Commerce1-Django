o
    ��dz  �                   @   s6   d dl mZmZ d dlZd dlZG dd� dej�ZdS )�    )�
migrations�modelsNc                   @   s�   e Zd ZdgZejddejej	j
jejjjjdd�dd�ejddejej	j
jejjjjd	d�dd�ejdd
ejej	j
jejjjjdd�dd�ejddejddddd�d�ejddejddgej	j
jdd�dd�ejddejddd�d�gZdS )�	Migration)�EcommerceappZ+0014_remove_products_product_brand_and_more�products�Price_FilterzEcommerceapp.price_filter)�default�	on_delete�toF)�
model_name�name�field�preserve_default�product_brandzEcommerceapp.brands�product_categoryzEcommerceapp.categories�
product_idT�d   )�blank�
max_length�null�unique)r   r   r   �stock)�IN STOCKr   )�OUT OF STOCKr   )�choicesr   r   �product_sub_category� �   )r   r   N)�__name__�
__module__�__qualname__�dependenciesr   �AddFieldr   �
ForeignKey�django�utils�timezone�now�db�deletion�CASCADE�	CharField�
AlterField�
operations� r.   r.   ��C:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0015_products_price_filter_products_product_brand_and_more.pyr      sL    ��������r   )�	django.dbr   r   �django.db.models.deletionr$   �django.utils.timezoner   r.   r.   r.   r/   �<module>   s   