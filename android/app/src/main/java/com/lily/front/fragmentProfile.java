package com.lily.front;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.fragment.app.Fragment;

public class fragmentProfile extends Fragment {

    private ImageView profilePic;
    private TextView name;
    private TextView email;
    private Button logout;

    public fragmentProfile() {
        // Constructor vacío obligatorio
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){

        // 1. Inflar el layout (MUY IMPORTANTE)
        View view = inflater.inflate(R.layout.fragment_profile, container, false);

        // 2. Vincular vistas
        profilePic = view.findViewById(R.id.profile_image);
        name = view.findViewById(R.id.therapist_name);
        email = view.findViewById(R.id.therapist_email);
        logout = view.findViewById(R.id.button_logout);
        // 3. Lógica básica (ejemplo)
        name.setText("Name Surname");
        email.setText("example@email.com");

        logout.setOnClickListener(v -> {
            // aquí iría tu lógica de logout
        });

        return view;
    }
}