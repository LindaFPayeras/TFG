import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.lily.front.R;

import androidx.fragment.app.Fragment;

public class activityMain extends AppCompatActivity{
    private BottomNavigationView navigationView;
    private Fragment fragment;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        // Creacion de la actividad
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);

        navigationView = findViewById(R.id.bottomAppBar);

        // Bottom Navigation
        navigationView.setOnItemSelectedListener(item -> {
            int itemId = item.getItemId();

            if (itemId == R.id.home){
                fragment = new fragmentPatients();
                return true;
            } else if (itemId == R.id.profile){
                fragment = new fragmentProfile();
                return true;
            }
            return false;
        });

    }

    // Cambiar de fragment
    private void loadFragment(Fragment fragment){
        getSupportFragmentManager()
                .beginTransaction()
                .replace(R.id.fragment_container, fragment)
                .addToBackStack(null)  // Permite volver sin que se me cierren los fragments
                .commit();
    }


}
