o
    I��c�  �                   @   s&   d dl mZmZ G dd� dej�ZdS )�    )�
migrations�modelsc                   @   s�   e Zd ZdgZejddejddddd�fdejd	d
�fdejddd�fdejddd�fdejdd
�fdej	dd�fdej
dd�fgd�gZdS )�	Migration)�EcommerceappZ0006_contact_email�Products�idTF�ID)�auto_created�primary_key�	serialize�verbose_name�product_name�2   )�
max_length�product_category� �   )�defaultr   �product_sub_category�product_desci�  �product_pricer   )r   �product_image�images)�	upload_to)�name�fieldsN)�__name__�
__module__�__qualname__�dependenciesr   �CreateModelr   �BigAutoField�	CharField�IntegerField�
ImageField�
operations� r&   r&   �]C:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0007_products.pyr      s    ����r   N)�	django.dbr   r   r   r&   r&   r&   r'   �<module>   s   