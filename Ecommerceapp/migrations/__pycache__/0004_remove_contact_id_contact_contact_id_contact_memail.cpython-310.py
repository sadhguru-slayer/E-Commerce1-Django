o
    X��c�  �                   @   s&   d dl mZmZ G dd� dej�ZdS )�    )�
migrations�modelsc                	   @   sV   e Zd ZdgZejddd�ejddejdddd	�dd
�ejddej	ddd�d�gZ
dS )�	Migration)�EcommerceappZ0003_remove_contact_email�contact�id)�
model_name�name�
contact_idr   TF)�default�primary_key�	serialize)r   r	   �field�preserve_default�memail�user��   )r   �
max_length)r   r	   r   N)�__name__�
__module__�__qualname__�dependenciesr   �RemoveField�AddFieldr   �	AutoField�
EmailField�
operations� r   r   ��C:\Users\sadgu\OneDrive\Desktop\Sippit-Folder\Sippit\Ecommerceapp\migrations\0004_remove_contact_id_contact_contact_id_contact_memail.pyr      s&    �����r   N)�	django.dbr   r   r   r   r   r   r   �<module>   s   