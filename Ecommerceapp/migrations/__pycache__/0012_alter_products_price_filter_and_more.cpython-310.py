o
    W�d�  �                   @   s.   d dl mZmZ d dlZG dd� dej�ZdS )�    )�
migrations�modelsNc                   @   s�   e Zd ZdgZejddejdej	jj
jdd�d�ejddejdej	jj
jd	d�d�ejdd
ejdej	jj
jdd�d�ejddejddd�d�ejddejddgddd�d�gZdS )�	Migration)�Ecommerceapp�90011_products_price_filter_products_created_date_and_more�products�Price_Filter�-zEcommerceapp.price_filter)�default�	on_delete�to)�
model_name�name�field�product_brandzEcommerceapp.brands�product_categoryzEcommerceapp.categories�product_sub_category�   )r
   �
max_length�stock)�IN STOCKr   )�OUT OF STOCKr   �d   )�choicesr
   r   N)�__name__�
__module__�__qualname__�dependenciesr   �
AlterFieldr   �
ForeignKey�django�db�deletion�CASCADE�	CharField�
operations� r&   r&   �yC:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0012_alter_products_price_filter_and_more.pyr      s:    �������r   )�	django.dbr   r   �django.db.models.deletionr    r   r&   r&   r&   r'   �<module>   s   