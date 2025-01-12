---
title: "Programming Languages"
---

# Programming Languages/Compilers/Interpreters

> Heavily inspired from
> [here](https://github.com/LesleyLai/learning/blob/main/pl.md)

## Theory

- [ ] [Theory of Computation by Michael Sipser](https://ocw.mit.edu/courses/mathematics/18-404j-theory-of-computation-fall-2020/)
- [ ] [Types and Programming Languages](https://mitpress.mit.edu/books/types-and-programming-languages)
- [ ] [Classical Papers in PL, recommendations](https://www.pls-lab.org/en/Classic_Papers_in_PL)
- [ ] [PL-Compilers-Resources](https://github.com/shining1984/PL-Compiler-Resource)
- [ ] [All you need is call/cc](http://pvk.ca/Blog/2013/09/19/all-you-need-is-call-slash-cc/)
- [ ] [Racket evaluation model(has a bit of stuff on continuation)](https://docs.racket-lang.org/reference/eval-model.html)
- [ ] [Racket continuations](https://docs.racket-lang.org/reference/cont.html)
- [ ] [Type System for Memory Safety(another banger by borretti)](https://borretti.me/article/type-systems-memory-safety)
- [ ] [Programming Languages Research (many papers and links consolidated here)](https://github.com/imteekay/programming-language-research)
- [ ] [How to read inference rules](https://cohost.org/prophet/post/2248211-how-to-read-inferenc)
- [ ] [How to implement effect handlers](https://cohost.org/prophet/post/3031893-it-doesn-t-actually?s=08)
- [ ] [How should I read type system notation?(by lexilambda)](https://langdev.stackexchange.com/questions/2692/how-should-i-read-type-system-notation/2693#2693)
- [ ] [ACM India summer School on PL and optimizations](https://archive.nptel.ac.in/courses/128/106/128106018/)
- [ ] [ACM India Summer School on Programming Languages(Thing of more interest is Program Semantics lectures(done in F\*))](https://archive.nptel.ac.in/courses/128/106/128106013/)
- [ ] [ACM Summer School on Compiler Design and construction(uses some llvm)](https://nptel.ac.in/courses/128106009)
- [ ] [PL Semantics by Graham Hutton](http://www.cs.nott.ac.uk/~pszgmh/123.pdf)
- [ ] [Getting Started with Category Theory](https://ryanbrewer.dev/posts/getting-started-category-theory/)
- [ ] [NUPRL - 10 papers that all PhD students in programming languages ought to know, for some value of 10](https://github.com/nuprl/10PL)
- [ ] [What does it mean for a type system or language to be "sound"?](https://langdev.stackexchange.com/questions/3372/what-does-it-mean-for-a-type-system-or-language-to-be-sound/3377#3377)
- [ ] [Normalization by Evaluation Four Ways: Reconstructing NbE Designs from First Principles](https://williamjbowman.com/tmp/nbe-four-ways/)
- [ ] [Parametric Higher-Order Abstract Syntax](https://lean-lang.org/lean4/doc/examples/phoas.lean.html) , [HOAS](http://adam.chlipala.net/cpdt/html/Hoas.html)
- [ ] [The precise definition of Normalization By Evaluation?](https://cstheory.stackexchange.com/questions/52149/the-precise-definition-of-normalization-by-evaluation)
- [ ] [Normalization by Evaluation, Agda](https://emmanueljs1.github.io/nbe/NbE.html)
- [ ] [Normalisation by Evaluation in the
Compilation of Typed Functional
Programming Languages - Sam Lindley Thesis](https://era.ed.ac.uk/bitstream/handle/1842/778/lindley_thesis.pdf?sequence=1&isAllowed=y)
- [ ] [Zulip Chat Archive - Subject Reduction](https://leanprover-community.github.io/archive/stream/113488-general/topic/subject.20reduction.html)
- [ ] [Zulip Chat Archive - What is the subject reduction debate?](https://leanprover-community.github.io/archive/stream/113488-general/topic/What.20is.20the.20subject.20reduction.20debate.3F.html)
- [ ] [Subject reduction in Lean](https://pixel-druid.com/articles/subject-reduction-in-lean.html)
- [ ] [How much of trouble is Lean's failure of normalization, given that logical consistency is not obviously broken?](https://proofassistants.stackexchange.com/questions/1183/how-much-of-trouble-is-leans-failure-of-normalization-given-that-logical-consi)

## Overview

- [ ] [Crafting Interpreter](http://www.craftinginterpreters.com/)
- [ ] [An Incremental Approach to Compiler Construction](http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf)
- [ ] [Let's Learn X86-64 Assembly](https://gpfault.net/posts/asm-tut-3.txt.html?s=08)

## Compiler Architecture

- [ ] [How the TypeScript Compiler Compiles - understanding the compiler internal](https://www.cs.cornell.edu/courses/cs6120/2020fa/self-guided/)
- [ ] [Anders Hejlsberg on Modern Compiler Construction](https://youtu.be/wSdV1M7n4gQ)
- [ ] [AOSA book: LLVM](https://aosabook.org/en/llvm.html)

## Parsing

- [x] [Simple but Powerful Pratt Parsing](https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html)

## JIT

- [ ] [Adventures in JIT Compilation](https://eli.thegreenplace.net/2017/adventures-in-jit-compilation-part-1-an-interpreter/)
- [ ] [Rhizome - a JIT for Ruby, implemented in pure Ruby](https://github.com/chrisseaton/rhizome)
- [ ] [Kipply's blog(lots of content relating to JIT)](https://kipp.ly/)

## Functional Languages

- [ ] [The Implementation of Functional Programming Languages](https://www.microsoft.com/en-us/research/wp-content/uploads/1987/01/slpj-book-1987-small.pdf) -
      by Simon Peyton Jones
- [ ] [Compiling Functional Languages to LLVM, a series(Lots of other cool articles as well in blog about typeclasses)](https://danieljharvey.github.io/posts/2023-02-08-llvm-compiler-part-1.html)

## GC

- [ ] [Baby's First Garbage Collector](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/)
- [ ] [The Garbage Collection Handbook](https://gchandbook.org/)
- [ ] [Oilshell "Pictures of a working garbage collector"(Goldmine for garbage collector stuff, see the whole blog)](https://news.ycombinator.com/item?id=34350260)
- [ ] Modern Garbage Collection(HN Discussion)
      [Part 1](https://news.ycombinator.com/item?id=13218550)
      [Part 2](https://news.ycombinator.com/item?id=21770530)
- [ ] [Boehm-Demers-Weiser Garbage Collector(Has papers linked in the GitHub repo)](https://news.ycombinator.com/item?id=35023833)
- [ ] [Understanding GC in JSC From Scratch](https://webkit.org/blog/12967/understanding-gc-in-jsc-from-scratch/)
- [ ] [Riptide,Webkit's GC](https://webkit.org/blog/7122/introducing-riptide-webkits-retreating-wavefront-concurrent-garbage-collector/)
- [ ] [High Performance GC for C++](https://v8.dev/blog/high-performance-cpp-gc)
- [ ] [Precise Stack Scanning in C++](https://docs.google.com/document/d/1mF-IW2UDwFslAREeapnP8bgXAlLG_DScOVhuTo34gBQ/edit#heading=h.ft3eufkln61m)
- [ ] [GC Resources, Thorsten Ball](https://gist.github.com/mrnugget/1fe234da53f436a16029a0fcd014201d)
- [ ] [Whippet, towards a new local maximum(more posts about GC present in the site)](https://wingolog.org/archives/2023/02/07/whippet-towards-a-new-local-maximum)
- [ ] [Deep Dive into ZGC, a modern garbage collector](https://dl.acm.org/doi/abs/10.1145/3538532)
- [ ] [Memory Allocation Strategies](https://www.gingerbill.org/series/memory-allocation-strategies/)
- [ ] [LuaJIT quad color GC](https://web.archive.org/web/20220107060536/http://wiki.luajit.org/New-Garbage-Collector)

## Compiler Optimizations

- [ ] [CS 6120: Advanced Compilers: The Self-Guided Online Course](https://www.cs.cornell.edu/courses/cs6120/2020fa/self-guided/)

## Educational Projects

- [ ] [chibcc by Rui Ueyama ](https://github.com/rui314/chibicc)
- [ ] [Multi-Language Programmable Linter](https://lobste.rs/s/pyrmyn/i_made_multi_language_programmable)
- [ ] [NEAL(Language agnostic code analysis tool)](https://github.com/uber/NEAL)
- [ ] [AST Grep tool](https://github.com/ast-grep/ast-grep)
- [ ] [Comby, Tool for searching and changing code structure](https://github.com/comby-tools/comby)
- [x] [Parser Parser Combinators(Talk about Comby)](https://youtu.be/JMZLBB_BFNg)
- [ ] [Making a Language(information about typechecker, looks good)](https://thunderseethe.dev/series/making-a-language/)
- [ ] [GCC Translation Validation(uses smt with gcc)](https://kristerw.github.io/2022/09/13/translation-validation/)
- [ ] [Not exactly educational, but FStar wiki seems very comprehensive(I want to read all of this sooo badly)](https://github.com/FStarLang/FStar/wiki)
- [ ] [Hackett by lexilambda](https://github.com/lexi-lambda/hackett)
- [ ] [labrys](https://github.com/kit-ty-kate/labrys)
- [ ] [llvm-tutor](https://github.com/banach-space/llvm-tutor)
- [ ] [lura(IDE focused programming language study)](https://github.com/aripiprazole/lura)
- [ ] [Soft(Lisp that compiles to LLVM)](https://github.com/aripiprazole/soft)
- [ ] [Wasm reference interpreter in OCaml](https://github.com/WebAssembly/spec/tree/main/interpreter)
- [ ] [Mukul Rathi's Bolt(has a series of blog posts explaining implementation)](https://github.com/mukul-rathi/bolt)
- [ ] [Carbon Design Documents](https://github.com/carbon-language/carbon-lang/tree/trunk/docs/design)
- [ ] [Trustfall(super cool thing)](https://github.com/obi1kenobi/trustfall)
- [ ] [Extensive tutorial of Hindley Milner](https://github.com/quchen/articles/blob/master/hindley-milner/README.md)
- [ ] [Write your own tiny programming system(s) (Hindley-Milner, OOP, Prolog,etc implementation)](https://d3s.mff.cuni.cz/teaching/nprg077/)
- [ ] [Type systems in ocaml](https://github.com/tomprimozic/type-systems)

## Virtual Machine

- [ ] [How to Build a Virtual Machine](https://youtu.be/OjaAToVkoTw)
- [ ] Small VMs and coroutines
      [HN](https://news.ycombinator.com/item?id=34420959)
      [Lobsters](https://lobste.rs/s/jrp9gv/small_vms_coroutines)
- [ ] Faster Virtual Machines
      [Lobsters](https://lobste.rs/s/cczkdj/faster_virtual_machines_speeding_up)
- [ ] [Interesting things about the Lua Interpreter(HN post link)](https://news.ycombinator.com/item?id=34213715)
- [ ] [Writing Interpreters in Rust](https://rust-hosted-langs.github.io/book/introduction.html)

## Misc Compilers

- [ ] [Cranelift Stuff(Reg Alloc, Instruction Selector etc, a series of blogs)](https://cfallin.org/)
- [ ] [Let's write a setjmp(HN Discussion)](https://news.ycombinator.com/item?id=34760828)
- [ ] [Design of Austral Compiler(See other articles as well to see more about typechecker)](https://borretti.me/article/design-austral-compiler)
- [ ] [What Austral Proves(Lobsters discussion and link)](https://lobste.rs/s/t4ifza/what_austral_proves)
- [ ] [Fibers, Oh My!](https://graphitemaster.github.io/fibers/)
- [ ] [Dmitry Vyukov — Go scheduler: Implementing language with lightweight concurrency](https://youtu.be/-K11rY57K7k)
- [ ] [Phil Eaton's Favourite Compiler and Interpreter Resources](https://lists.eatonphil.com/compilers-and-interpreters.html)
- [ ] [JVM Internals by Aleksey Shipilev](https://shipilev.net/jvm/anatomy-quarks/)
- [ ] [Max Bernstein(tekknolagi) pl resources](https://bernsteinbear.com/pl-resources/)
- [ ] [A lisp compiler and interpreter writing series by tekknolagi](https://bernsteinbear.com/blog/lisp/)
- [ ] [How to compile with continutations](https://matt.might.net/articles/cps-conversion/)
- [ ] [Design roadmap about YSH(by oilshell guy)](http://www.oilshell.org/blog/2023/06/ysh-review.html)
- [ ] [Tao programming language(has so many cool features,see how they're implemented)](https://github.com/zesterer/tao)
- [ ] [Alexis King - “Effects for Less” @ ZuriHac 2020(content is just madd)](https://www.youtube.com/live/0jI-AlWEwYI?feature=share)
      ,
      [GHC proposal link](https://github.com/ghc-proposals/ghc-proposals/pull/313)
- [ ] [Blog for Kalyn(Compiled Typed Haskell like Lisp)](https://intuitiveexplanations.com/tech/kalyn)
- [ ] [Alexis King - "Delimited Continuations, Demystified"](https://youtu.be/TE48LsgVlIU),
      [same talk ZuriHac 2023](https://youtu.be/DRFsodbxHQo)
- [ ] [GHC Reading List](https://gitlab.haskell.org/ghc/ghc/-/wikis/reading-list)
- [ ] [Mapping High level constructs to LLVM IR](https://github.com/f0rki/mapping-high-level-constructs-to-llvm-ir)
- [ ] [Program Analysis Resources(very comprehensive)](https://gist.github.com/MattPD/00573ee14bf85ccac6bed3c0678ddbef)
- [ ] [Learning Resources for Clang libraries](https://discourse.llvm.org/t/new-learning-resource-for-clang-libraries-slide-deck-and-code-examples/67604)
- [ ] [Compiler Optimizations](https://compileroptimizations.com/index.html)
- [ ] [Algebraic Effects for the Rest of Us](https://overreacted.io/algebraic-effects-for-the-rest-of-us/)

## Linkers

- [ ] [Mold(README has a lot of information)](https://github.com/rui314/mold)
- [ ] [How to execute an object file](https://blog.cloudflare.com/how-to-execute-an-object-file-part-4/)

## Courses and Assignments

- [ ] [CIS 341 - Compilers(Has very nice assignments) ](https://www.seas.upenn.edu/~cis341/current/)
- [ ] [CSE 131 - Compiler Construction(Haskell) ](https://podcast.ucsd.edu/watch/wi18/cse131_a00/5/screen)
- [ ] [CSE 131 - Compiler Construction(Ocaml) ](https://ucsd-cse131-f19.github.io/)
- [ ] [CSE 131/231- Compiler Construction(Rust)](https://ucsd-compilers-s23.github.io/index.html#schedule)
- [ ] [CMU Compilers Course by Jan Hoffman](https://www.cs.cmu.edu/~janh/courses/411/23/)
- [ ] [Essentials of Compilation Course and Book](https://github.com/IUCompilerCourse/Essentials-of-Compilation)
- [ ] [Course on VMs and Managed Runtimes](http://www.wolczko.com/CS294/)
- [ ] [(Book)Design and semantics of PL, in Scala](https://ps-tuebingen-courses.github.io/pl1-lecture-notes/01-intro/intro.html)
- [ ] [Programs and Proofs](https://kcsrk.info/cs6225_s21_iitm/)
- [ ] [Software Foundations(Course Cornell)](https://youtube.com/playlist?list=PLre5AT9JnKShFK9l9HYzkZugkJSsXioFs)
- [ ] [Software Foundations Books](https://softwarefoundations.cis.upenn.edu/index.html)
- [ ] [An introduction to creating a C compiler for those who want to know the lower layers(In Japanese, so have to translate)](https://www-sigbus-info.translate.goog/compilerbook?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en)
- [ ] [PL Class by Edward Z Yangz](https://youtube.com/playlist?list=PL9sqUxos-K_dOV8k2q6JZN-u78BNJVhwd),
      [materials link( i think )](https://github.com/ezyang/pl-class-public)
- [ ] [Advanced Functional Programming(in Agda with videos)](https://github.com/pigworker/CS410-18/tree/master?s=08)
- [ ] [Programming languages(follows TAPL and content looks great)](https://www3.nd.edu/~dchiang/teaching/pl/2022/index.html)
- [ ] [Xavier Leroy - Program logics: reasoning principles for high-assurance software](https://xavierleroy.org/CdF/2020-2021/)
- [ ] [Xavier Leroy - Mechanized semantics: when machines reason about their languages](https://xavierleroy.org/CdF/2019-2020/index.html)
- [ ] [Xavier Leroy - Programming = proving? The Curry-Howard correspondence today](https://xavierleroy.org/CdF/2018-2019/index.html)
- [ ] [Xavier Leroy - Control structures](https://xavierleroy.org/CdF/2023-2024/index.html)


## Theorem Provers

- [ ] [Logic and Proofs in Lean(3?)](https://leanprover.github.io/logic_and_proof/index.html)
- [ ] [Theorem Proving in Lean4](https://lean-lang.org/theorem_proving_in_lean4/)
- [ ] [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/index.html)
- [ ] [Mechanics of Proofs](https://hrmacbeth.github.io/math2001/)
- [ ] [What is the difference between Gallina and Ltac?](https://coq.discourse.group/t/what-is-the-difference-between-gallina-and-ltac/1184)
- [ ] [Coq <-> Lean4 Tactics Cheat Sheet](https://gist.github.com/watersofoblivion/9646164deb5c1901413d64ba9f2a49b9#file-tacticscheatsheet-md)
- [ ] [Lean Tactic Reference](https://course.ccs.neu.edu/cs2800sp23/ref.html)
- [ ] [Logic and Computation Course, uses Lean 4](https://course.ccs.neu.edu/cs2800sp23/index.html)
- [ ] [Lean 3 Type theory](https://github.com/digama0/lean-type-theory)
- [ ] [Typechecking in Lean4](https://ammkrn.github.io/type_checking_in_lean4/title_page.html)
- [ ] [Lean4Lean](https://github.com/digama0/lean4lean)
- [ ] [Semantics Course in Coq/Rocq - Saarland University ](https://gitlab.mpi-sws.org/FP/semantics-course/)
- [ ] [A Logical Approach to Type Soundness](https://iris-project.org/pdfs/2024-jacm-logical-type-soundness.pdf)
- [ ] [Iris Tutorial](https://github.com/logsem/iris-tutorial?tab=readme-ov-file) , [Iris Lecture Notes](https://iris-project.org/tutorial-material.html)
- [ ] [PulseCore: A Dependently Typed Stratified Separation Logic](https://fstar-lang.org/papers/pulsecore.pdf)
- [ ] [Hitchhiker's Guide to Logical Verification - Lean4](https://github.com/lean-forward/logical_verification_2024)

## Some Cool stuff I've found

- [ ] [How does this work??? (Mulligan)](https://github.com/brandonspark/mulligan)
- [ ] [Garbage collection with zero cost at non-GC time](https://gist.github.com/AndrasKovacs/fc9e20b0976b7e236b5899fde8f5c95d?s=08)
- [ ] [Why is Idris 2 much faster than Idris 1?](https://www.type-driven.org.uk/edwinb/why-is-idris-2-so-much-faster-than-idris-1.html?s=08)
- [ ] [Making more out of traits(Rust)](https://internals.rust-lang.org/t/making-more-out-of-traits/5796)  and [many other discussion about Rust language design](https://internals.rust-lang.org/c/language-design/21)
- [ ] [New research programming languages thread Reddit](https://www.reddit.com/r/ProgrammingLanguages/s/uufTftvdLu)

## Dependent Types

- [ ] [A tutorial implementation of a dependently typed lambda calculus (LambdaPi)](https://www.andres-loeh.de/LambdaPi/)
- [ ] [OCaml Discuss - Dependent Types in the Purest Form](https://discuss.ocaml.org/t/dependent-types-in-the-purest-form/10547/7)
- [ ] [Swift Discuss - [Pitch] Dependent Types & Universes (Stage 1 of Proof-Driven Development?)](https://forums.swift.org/t/pitch-dependent-types-universes-stage-1-of-proof-driven-development/63754)
- [ ] [Dependent Theory of Types](https://ice1000.org/dtt-dev/assemble.html)
- [ ] [Online reference book for *implementing* concepts in type theory, Answererd by Andras Kovacs](https://math.stackexchange.com/questions/3466976/online-reference-book-for-implementing-concepts-in-type-theory)

## Automated Verification

- [ ] [Automated Program Verification - Waterloo](https://ece.uwaterloo.ca/~agurfink/ece750t29/)
- [ ] [Automated Program Verification - Kartik Nagar](https://kartiknagar.github.io/courses/apv/lectures/)
- [ ] [Modern Symbolic AI and Automated Reasoning](https://kmicinski.com/cis700-f23/)
