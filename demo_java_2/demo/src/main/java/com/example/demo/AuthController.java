// package com.example.demo;

// import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.web.bind.annotation.*;
// import org.springframework.security.authentication.AuthenticationManager;




// @RestController
// @RequestMapping("/api")
// public class AuthController {

//     @Autowired
//     private JwtUtil jwtUtil;

//     @Autowired
//     private AuthenticationManager authenticationManager;

//     @PostMapping("/authenticate")
//     public ResponseEntity<?> createAuthenticationToken(@RequestBody AuthRequest authRequest) throws Exception {
//         try {
//             authenticationManager.authenticate(
//                     new UsernamePasswordAuthenticationToken(authRequest.getUsername(), authRequest.getPassword())
//             );
//         } catch (BadCredentialsException e) {
//             throw new Exception("Incorrect username or password", e);
//         }

//         final UserDetails userDetails = userService.loadUserByUsername(authRequest.getUsername());
//         final String jwt = jwtUtil.generateToken(userDetails.getUsername());

//         return ResponseEntity.ok(new AuthResponse(jwt));
//     }

//     // Other endpoints...
// }
