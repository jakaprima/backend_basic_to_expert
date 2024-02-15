// package com.example.demo;

// import java.util.ArrayList;
// import java.util.List;

// import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.web.bind.annotation.*;
// import com.example.demo.Book;


// import java.util.List;

// @RestController
// @RequestMapping("/api/books")
// public class BookController {
//     // @Autowired
//     // private BookService bookService;

//     @GetMapping
//     public List<Book> getAllBooks() {
//         // return bookService.getAllBooks();
//         List<Book> books = new ArrayList<>();
//         books.add(new Book(1L, "Book 1", "Author 1"));
//         books.add(new Book(2L, "Book 2", "Author 2"));
//         return books;
//     }

//     // @GetMapping("/{id}")
//     // public Book getBookById(@PathVariable Long id) {
//     //     return bookService.getBookById(id);
//     // }

//     // @PostMapping
//     // public Book saveBook(@RequestBody Book book) {
//     //     return bookService.saveBook(book);
//     // }

//     // @DeleteMapping("/{id}")
//     // public void deleteBook(@PathVariable Long id) {
//     //     bookService.deleteBook(id);
//     // }
// }
