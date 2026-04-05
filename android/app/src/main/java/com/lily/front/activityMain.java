package com.lily.front;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.bottomnavigation.BottomNavigationView;

import androidx.fragment.app.Fragment;

public class activityMain extends AppCompatActivity{
    private BottomNavigationView navigationView;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        navigationView = findViewById(R.id.bottomAppBar);

        // Cargar fragmento inicial
        if (savedInstanceState == null) {
            loadFragment(new fragmentPatients());
        }

        // Bottom Navigation
        navigationView.setOnItemSelectedListener(item -> {
            int itemId = item.getItemId();

            if (itemId == R.id.home){
                loadFragment(new fragmentPatients());
                return true;
            } else if (itemId == R.id.profile){
                loadFragment(new fragmentProfile());
                return true;
            }
            return false;
        });
    }

    // Cambiar de fragment
    private void loadFragment(Fragment fragment){
        if (fragment != null) {
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.fragment_container, fragment)
                    .commit();
        }
    }
}