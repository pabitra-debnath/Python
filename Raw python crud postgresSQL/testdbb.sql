PGDMP         2                w            testdbb    11.3    11.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    16416    testdbb    DATABASE     �   CREATE DATABASE testdbb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE testdbb;
             postgres    false            �            1259    16417    role    TABLE     ,  CREATE TABLE public.role (
    id integer NOT NULL,
    role character varying,
    orderr character varying,
    version character varying,
    "createdBy" character varying,
    "createdOn" timestamp without time zone,
    "updatedBy" character varying,
    "updatedOn" timestamp with time zone
);
    DROP TABLE public.role;
       public         postgres    false            �            1259    16425    userr    TABLE     m  CREATE TABLE public.userr (
    id integer NOT NULL,
    name character varying,
    age integer,
    gender character varying,
    roleid integer,
    orderr character varying,
    version character varying,
    "createdBy" character varying,
    "createdOn" timestamp with time zone,
    "updatedBy" character varying,
    "updatedOn" timestamp with time zone
);
    DROP TABLE public.userr;
       public         postgres    false            �
          0    16417    role 
   TABLE DATA               m   COPY public.role (id, role, orderr, version, "createdBy", "createdOn", "updatedBy", "updatedOn") FROM stdin;
    public       postgres    false    196   �                  0    16425    userr 
   TABLE DATA               �   COPY public.userr (id, name, age, gender, roleid, orderr, version, "createdBy", "createdOn", "updatedBy", "updatedOn") FROM stdin;
    public       postgres    false    197   G       �
           2606    16424    role role_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.role DROP CONSTRAINT role_pkey;
       public         postgres    false    196            �
           2606    16432    userr userr_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.userr
    ADD CONSTRAINT userr_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.userr DROP CONSTRAINT userr_pkey;
       public         postgres    false    197            �
           2606    16433    userr roleid_too_userr    FK CONSTRAINT     s   ALTER TABLE ONLY public.userr
    ADD CONSTRAINT roleid_too_userr FOREIGN KEY (roleid) REFERENCES public.role(id);
 @   ALTER TABLE ONLY public.userr DROP CONSTRAINT roleid_too_userr;
       public       postgres    false    197    2690    196            �
   �   x�M�]�0���w���@�	x)?j-M�!zz���>l��f2�M1��S�:���xB�f�Qݠu���e���`� 	C8�1�����l�zO�ÅzP��1G�$7<-q��Iz��h��f�8	�cA���r~4k�HT�*�X%�Ĭ%v=$d�wҍ��M���^C�(KRTg�� S�             x������ � �     