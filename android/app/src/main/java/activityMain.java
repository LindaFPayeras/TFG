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
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);

        navigationView = findViewById(R.id.bottomAppBar);

        // Bottom Navigation
        navigationView.setOnItemSelectedListener(item -> {
            int itemId = item.getItemId();

            if (itemId == R.id.home){
                fragment = new fragmentHome();
                return true;
            } else if (itemId == R.id.profile){
                fragment = new fragmentProfile();
                return true;
            }
            return false;
        });




    }
}
