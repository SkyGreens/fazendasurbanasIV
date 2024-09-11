package com.skygreen.SkyGreen.entities;

import java.util.Collection;
import java.util.List;

import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.br.CPF;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Email;
import lombok.Data;


@Data
@Entity(name = "funcionario")
@Table(name = "funcionario")
public class FuncionarioEntity implements UserDetails {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Length(max = 30, message = "Limite de 30 caracteres excedido")
    private String senha;
    private Boolean ativo;
    @Email
    private String email;

    private FuncionarioRole role;

    @Length(max = 50, message = "Limite de 50 caracteres excedido")
    private String nome;
    @CPF
    private String cpf;


    @Override
    public Collection<? extends GrantedAuthority> getAuthorities(){
       if(this.role == FuncionarioRole.ADMIN) return List.of(new SimpleGrantedAuthority("ROLE_ADMIN"), new SimpleGrantedAuthority("ROLE_GERENTEPRODUCAO"), new SimpleGrantedAuthority("ROLE_ASSISTENTEADMINISTRATIVO"));
       else if(this.role == FuncionarioRole.ASSISTENTEADMINISTRATIVO) return List.of(new SimpleGrantedAuthority("ROLE_ASSISTENTEADMINISTRATIVO"));
       else return List.of(new SimpleGrantedAuthority("ROLE_GERENTEPRODUCAO"));
    }

    @Override
    public String getUsername(){
        return cpf;
    }
    
    @Override
    public String getPassword() {
        return senha;
    }
    @Override
    public boolean isAccountNonExpired(){
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
     }
     
     @Override
     public boolean isEnabled() {
        return true;
     }
    
     @Override
     public boolean isAccountNonLocked() {
        return true;
     }


}
