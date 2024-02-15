package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
	"strings"
	"github.com/dgrijalva/jwt-go"
)

var SECRET_KEY_APP = []byte("25a2aaaed449c7d3125c9fd6d3131e109f6531f35db1c519b4c1ee6a3352dc85")

type Credentials struct {
	Username string `json: "username"`
	Password string `json: "password"`
}

type Claims struct {
	Username string `json: "username"`
	jwt.StandardClaims
}

func login(w http.ResponseWriter, r *http.Request) {
	var creds Credentials

	err := json.NewDecoder(r.Body).Decode(&creds)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	if creds.Username == "jaka prima maulana" && creds.Password == "admin@1234" {
		// create jwt token dengan username sebagai claim
		expirationTime := time.Now().Add(5 * time.Minute)
		claims := &Claims{
			Username: creds.Username,
			StandardClaims: jwt.StandardClaims{
				ExpiresAt: expirationTime.Unix(),
			},
		}
		token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

		tokenString, err := token.SignedString(SECRET_KEY_APP)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		w.Write([]byte(tokenString))
	} else {
		w.WriteHeader(http.StatusUnauthorized)
		return
	}
}

func authenticate(next http.Handler) http.Handler {
	return http.HandlerFunc(func (w http.ResponseWriter, r *http.Request) {
		tokenString := strings.Replace(r.Header.Get("Authorization"), "Bearer ", "", -1)
		if tokenString == "" {
			w.WriteHeader(http.StatusUnauthorized)
			return
		}

		token, err := jwt.ParseWithClaims(tokenString, &Claims{}, func(token *jwt.Token) (interface{}, error) {
			return SECRET_KEY_APP, nil
		})
		if err != nil || !token.Valid {

			fmt.Println("ERR", err.Error())
			w.WriteHeader(http.StatusUnauthorized)
			return
		}

		next.ServeHTTP(w, r)

	})
}



func protected(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Welcome to protected endpoint"))
}


func main() {
	http.HandleFunc("/login", login)
	http.Handle("/protected", authenticate(http.HandlerFunc(protected)))

	fmt.Println("Server is running on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}