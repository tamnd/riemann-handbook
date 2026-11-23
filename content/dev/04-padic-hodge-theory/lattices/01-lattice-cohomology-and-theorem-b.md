---
title: Lattice cohomology and the local Theorem B
decls:
  - Formalism.MainNotions.N.Ln17.thmB_at
  - Formalism.MainNotions.N.Ln17.frobenius_statement_of_inputs
  - Formalism.MainNotions.N.Ln17.stmt_holds
  - Formalism.MainNotions.N.Ln17.frobenius_statement_of_fontaine
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattice cohomology and the local Theorem B

Let $F \colon T_1 \to T_2$ be a map of Galois-stable lattices in two crystalline representations, and assume that $F$ is onto. A finite class of $T_2$ need not come from a finite class of $T_1$. This section defines the colength that measures this, and proves the local Theorem B: when the Hodge-Tate jumps of $T_1$ sit in narrow windows, one for each embedding of the unramified field $K$, the colength is bounded by an explicit expression in the windows, times the length of $\mathcal{O}/p\mathcal{O}$. The theorem is used in [Theorem B of admitted inputs](/entry/theorem-b-of-admitted-inputs/).

**Definition 8.1.1 (Period datum).** A *period datum* consists of a prime $p$, a group $G$, finite extensions $K_0 \subseteq K$ of a field $\mathbb{Q}_p$, and two rings $B$ and $B_{\mathrm{dR}}$ with the following structure. The group $G$ acts on $B$ by $K_0$-algebra automorphisms and on $B_{\mathrm{dR}}$ by $K$-algebra automorphisms, with $B^G = K_0$ and $B_{\mathrm{dR}}^G = K$. There is an injective Frobenius $\varphi$ of $B$ that commutes with $G$ and acts on $K_0$ as a fixed automorphism $\sigma$. There is an injective $G$-equivariant $K_0$-algebra map $B \to B_{\mathrm{dR}}$. Finally $B_{\mathrm{dR}}$ has a decreasing filtration $(\mathrm{Fil}^a)_{a \in \mathbb{Z}}$ by $K$-subspaces with $1 \in \mathrm{Fil}^0$ and $\mathrm{Fil}^a \cdot \mathrm{Fil}^b \subseteq \mathrm{Fil}^{a+b}$.

These are the properties of the [period rings](/learn/galois-representations/#period-rings) $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ of Fontaine for $G = G_K$ that the chapter uses. In the application $K_0$ is the maximal unramified subfield of $K$. We write $n = [K_0 : \mathbb{Q}_p]$.

Let $L$ be a finite extension of $\mathbb{Q}_p$, the field of coefficients, and let $\mathcal{O}$ be the integral closure of $\mathbb{Z}_p$ in $L$; it is a [discrete valuation ring](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices). Let $V$ be a finite-dimensional $L$-vector space with a continuous $L$-linear action $\rho$ of $G$.

**Definition 8.1.2 (Lattice).** A *lattice* in $V$ is an $\mathcal{O}$-submodule $T \subseteq V$ that is stable under $\rho(G)$, finitely generated and free over $\mathcal{O}$, and spans $V$ over $L$.

For a lattice $T$ we use [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology) with values in $T$. Let $Z^1(T)$ be the $\mathcal{O}$-module of continuous $1$-cocycles $c \colon G \to V$ with $c(gh) = c(g) + \rho(g)c(h)$ and with all values in $T$. Let $B^1(T)$ be the module of coboundaries $g \mapsto \rho(g)x - x$ with $x \in T$. A continuous cocycle $c$ is *finite* if it becomes a coboundary over $B$: there is $x \in V \otimes_{\mathbb{Q}_p} B$ with $c(g) \otimes 1 = g x - x$ for all $g \in G$, Let $Z^1_f(T) \subseteq Z^1(T)$ be the finite cocycles with values in $T$. Its image in $H^1(T) = Z^1(T)/B^1(T)$ is the module $H^1_f(T)$ of finite classes.

**Definition 8.1.3 (Map of lattices, colength).** Let $T_1 \subseteq V_1$ and $T_2 \subseteq V_2$ be lattices. A *map of lattices* $F \colon T_1 \to T_2$ is a continuous $G$-equivariant $L$-linear map $F \colon V_1 \to V_2$ with $F(T_1) \subseteq T_2$. It is *onto* if $F(T_1) = T_2$. Let
$$\operatorname{Im}_F = F_*\bigl(Z^1_f(T_1)\bigr) + B^1(T_2),$$
where $F_* c = F \circ c$. The *colength* of $F$ is
$$\operatorname{col}(F) = \operatorname{length}_{\mathcal{O}} \Bigl( Z^1_f(T_2) \big/ \bigl(\operatorname{Im}_F \cap Z^1_f(T_2)\bigr) \Bigr) \in \mathbb{N} \cup \{\infty\}.$$
For $e \in \mathbb{N}$ we say that $F$ *lifts with exponent* $e$ if $p^e c \in \operatorname{Im}_F$ for all $c \in Z^1_f(T_2)$. For $x \in \mathbb{R}$ we write $\operatorname{col}(F) \le x \cdot \lambda$ if $\operatorname{col}(F)$ is finite and $\operatorname{col}(F) \le x \cdot \lambda$, with $\lambda = \operatorname{length}_{\mathcal{O}}(\mathcal{O}/p\mathcal{O})$.

The colength is the [length](/learn/algebra/#rings-ideals-and-modules) of the cokernel of $F_*$ on finite classes. The number $\lambda$ is the ramification index of $L$ over $\mathbb{Q}_p$, so the bounds do not depend on the ramification of $L$.

**Definition 8.1.4 (Hodge-Tate jumps).** Let $D_{\mathrm{cris}}(V) = (V \otimes_{\mathbb{Q}_p} B)^G$ and $D_{\mathrm{dR}}(V) = (V \otimes_{\mathbb{Q}_p} B_{\mathrm{dR}})^G$. The representation is *crystalline* if $\dim_L D_{\mathrm{cris}}(V) = n \dim_L V$. For an embedding $\tau \colon K \to L$ let $D_{\mathrm{dR},\tau}$ be the $\tau$-part of $D_{\mathrm{dR}}(V)$ and $\mathrm{Fil}^a_\tau = D_{\mathrm{dR},\tau} \cap (V \otimes \mathrm{Fil}^a)$. An integer $a$ is a *jump* at $\tau$ if $\mathrm{Fil}^{a+1}_\tau \ne \mathrm{Fil}^a_\tau$, and its *multiplicity* is $\dim \mathrm{Fil}^a_\tau - \dim \mathrm{Fil}^{a+1}_\tau$.

For crystalline $V$ these are the Hodge-Tate weights of $V$ at $\tau$, up to the sign convention; see [crystalline and de Rham representations](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations). A lattice is crystalline if the representation it spans is.

**Definition 8.1.5 (Letters).** Fix a bijection $i \mapsto \mathrm{emb}_i$ from $\mathbb{Z}/n$ onto the set of $\mathbb{Q}_p$-embeddings $K_0 \to L$, with $\mathrm{emb}_{i+1} \circ \sigma = \mathrm{emb}_i$. The elements of $\mathbb{Z}/n$ are the *letters*. An embedding $\tau \colon K \to L$ lies *over* the letter $i$ if $\tau|_{K_0} = \mathrm{emb}_i$. For a lattice $T$, a letter $i$ and a set $S \subseteq \mathbb{Z}$, the jumps of $T$ *at $i$ lie in* $S$ if for every $\tau$ over $i$ every jump at $\tau$ is in $S$. For maps $M, h \colon \mathbb{Z}/n \to \mathbb{N}$ the jumps of $T$ are *bounded by* $(M, h)$ if the jumps at each letter $i$ lie in $[-M_i, h_i]$.

For a level $s \ge 1$ we say $(K, L)$ is *good at level $s$* if $p = 2$ forces $s \ge 2$, $K \subseteq K_0(\mu_{p^s})$, and every embedding of $K_0(\mu_{p^s})$ lands in $L$. We are in *case A* if $K$ lies in the maximal unramified extension of $\mathbb{Q}_p$, $p \ne 2$, and $(K, L)$ is good at level $1$. In case A the map $K_0 \to K$ is a bijection, so $K = K_0$ and $n = [K : \mathbb{Q}_p]$.

**Definition 8.1.6 (Setting of Theorem B).** Let $F \colon T_1 \to T_2$ be a map of lattices, $b, w, S, \eta, m \in \mathbb{N}$, a sign $\mathrm{up} \colon \mathbb{Z}/n \to \{\text{true}, \text{false}\}$, and sizes $\mathrm{size}, M, h \colon \mathbb{Z}/n \to \mathbb{N}$. A letter $i$ is *thick* if $b \le \mathrm{size}_i \le b + \eta$. We are in the *setting of Theorem B* if:

1. we are in case A, $T_1$ and $T_2$ are crystalline, and $F$ is onto;
2. $\eta < \mathrm{size}_i$ for every letter $i$;
3. the jumps of $T_1$ at $i$ lie in $[\mathrm{size}_i, \mathrm{size}_i + S] \cup [-\eta, \eta]$ if $\mathrm{up}_i$ holds, and in $[-\mathrm{size}_i - S, -\mathrm{size}_i] \cup [-\eta, \eta]$ otherwise;
4. for each letter $i$, the sum over $\tau$ over $i$ and over $a \in [-\eta, \eta]$ of the multiplicity of $a$ for $T_2$ is at most $m$;
5. every letter that is not thick has $\mathrm{size}_i \le w$;
6. the jumps of $T_1$ are bounded by $(M, h)$.

So each letter carries a window of width $S$ far from $0$, above or below, and a central band $[-\eta, \eta]$. Put
$$h_B = \begin{cases} b + \eta + S & \text{if some letter is thick,} \\ w + S & \text{otherwise.} \end{cases}$$
For a constant $C$ and $\lambda_g = \log_p(2 h_B)$, the *band condition* holds if there is a letter $i$ that is not thick, with $i + 1$ or $i - 1$ thick, such that
$$\bigl| p \cdot \mathrm{size}_i - b \bigr| \le C \bigl( p\eta + pS + b/p + \mathrm{size}_i + p \lambda_g \bigr).$$
Set $\beta = 1$ if the band condition holds and $\beta = 0$ otherwise.

**Definition 8.1.7 (Lifting exponent).** For a prime $l$ and $H \in \mathbb{N}$ let
$$e_W(l, H) = \Bigl\lfloor \frac{Hl}{(l-1)^2} + 3 + \log_l (H+1) \Bigr\rfloor.$$
For $M \in \mathbb{N}$ let $a(l, M) = \lfloor M/(l-1) \rfloor + 1$. For a finite set $J \subseteq \mathbb{Z}$ let $J^{+M}$ be the set of nonzero integers $j + t$ with $j \in J$ and $1 \le t \le M$, together with $1, \dots, M$, and
$$e_U(l, M, J) = \sum_{j \in J^{+M}} v_l(j) + a(l, M) + v_l\bigl(a(l, M)!\bigr).$$
For a lattice $T_1$ with jumps bounded by $(M, h)$, let $M^* = \max_i M_i$, $h^* = \max_i h_i$, $H^* = \max_i (M_i + h_i)$, and let $J$ be the set of jumps of $T_1$, at any $\tau$, in $[-M^*, h^*]$. The *lifting exponent* is
$$e'(T_1) = 2 e_W(p, H^*) + e_U(p, M^*, J).$$

So $e'(T_1)$ depends only on $p$ and on the jumps of $T_1$, and grows linearly in the largest jump. We take two results as given. Both are parts of the admitted inputs of the local theory, and both concern a single pair $(K, L)$.

**Theorem 8.1.8 (Lifting in case A).** In case A, let $F \colon T_1 \to T_2$ be a map of crystalline lattices that is onto, with the jumps of $T_1$ bounded by $(M, h)$. Then $F$ lifts with exponent $e'(T_1)$.

This is taken as an input. It belongs to the theory of Wach modules (Wach, *Représentations p-adiques potentiellement cristallines*; Berger, *Limites de représentations cristallines*); the chapter does not prove it. The [lifting theorem E](/entry/theorem-e-final-form/) of the second part proves a lifting statement of the same kind along arcs, with another exponent.

**Theorem 8.1.9 (Generators of finite classes).** Assume $K_0 \to K$ is a bijection and let $T$ be a crystalline lattice in $V$. Then $H^1_f(T)$ is generated over $\mathcal{O}$ by at most $(n + 1)\dim_L V$ classes.

This is taken as an input. Over $L$ it follows from the dimension formula $\dim H^1_f(V) = \dim D_{\mathrm{dR}}(V)/\mathrm{Fil}^0 + \dim H^0(V)$ of Bloch and Kato, *L-functions and Tamagawa numbers of motives*, Corollary 3.8.4, since in case A the two terms are at most $n \dim V$ and $\dim V$. The integral statement is taken as given.

**Theorem 8.1.10 (Local Theorem B).** Let $C \ge 320$. Let $p = \ell$ be a prime with $\ell \ge 11$, let $K$ and $L$ be finite extensions of $\mathbb{Q}_\ell$ in case A, and fix the admitted inputs of the local theory. Let the data be in the setting of Theorem B, with $20w \le b$, $20\eta \le b$, $20S \le b$, and with at least one letter that is not thick. Let $r = \dim_L V_2$, $\lambda_g = \log_\ell(2h_B)$, and $e' = e'(T_1)$.

(a) Assume that $\mathrm{up}_{i+1} \ne \mathrm{up}_i$ for every letter $i$, and that no three consecutive letters $i, i+1, i+2$ are all thick. Then $\operatorname{col}(F) \le x_a \cdot \lambda$ with
$$\begin{aligned} x_a = {} & C(n+1) r \Bigl( \frac{h_B}{\ell^2} + \frac{w + \eta}{\ell} + S + 1 + \lambda_g + \eta \beta \Bigr) \\ & + C n m e'. \end{aligned}$$

(b) Let $R \ge 1$. Assume that $\mathrm{up}$ is constant and that no $R$ consecutive letters $i, \dots, i + R - 1$ are all thick. Then $\operatorname{col}(F) \le x_b \cdot \lambda$ with
$$\begin{aligned} x_b = {} & C(n+1) r \Bigl( \frac{h_B}{\ell^2} + \frac{w + \eta}{\ell} + R^2 (S + 1 + \lambda_g) + \eta \beta \Bigr) \\ & + C n m R^2 e'. \end{aligned}$$

Lean: `Formalism.MainNotions.N.Ln17.thmB_at`.

*Proof.* Put
$$\Sigma = \frac{h_B}{\ell^2} + \frac{w + S + \eta}{\ell} + \lambda_g + 1.$$
Three facts give the bound. First, by the theorem on generators of finite classes, $H^1_f(T_2)$ has at most $g = (n+1) r$ generators. Second, by lifting in case A, $F$ lifts with exponent $e'$. Third, a counting step: let $e, e_1 \in \mathbb{N}$ and let $Z \subseteq Z^1_f(T_2)$ be finite, such that $p^e c \in \operatorname{Im}_F + \operatorname{span}_{\mathcal{O}} Z$ for all $c \in Z^1_f(T_2)$, and $F$ lifts with exponent $e_1$. Then $\operatorname{col}(F) \le (g e + |Z| e_1) \lambda$. Indeed, the quotient $Z^1_f(T_2)/(\operatorname{Im}_F \cap Z^1_f(T_2))$ is generated by the images of the $g$ generators and of $Z$; the first are killed by $p^e$ modulo the span of $Z$, the second by $p^{e_1}$, and a cyclic module killed by $p^k$ over the discrete valuation ring $\mathcal{O}$ has length at most $k\lambda$.

It remains to find $e$ and $Z$ in each case. In case (a) assume first that some letter is thick and $b/4 < 40\Sigma$. A lemma for this case, proved from the admitted inputs, shows that $F$ lifts with an exponent $e_0 \le 160 \Sigma$. The counting step with $e = e_1 = e_0$ and $Z = \emptyset$ gives $\operatorname{col}(F) \le 160 g \Sigma \lambda$. Since $S/\ell \le S$, the number $\Sigma$ is at most the bracket in $x_a$, and $160 \le C$. Otherwise no letter is thick, or $40\Sigma \le b/4$. Then [the sum along alternating arcs](/entry/sum-alt/) gives $e \le 55\Sigma + 13S + \eta\beta$ and a set $Z$ of at most $4nm$ finite cocycles with $p^e Z^1_f(T_2) \subseteq \operatorname{Im}_F + \operatorname{span} Z$. The counting step with $e_1 = e'$ gives
$$\operatorname{col}(F) \le \bigl( g (55\Sigma + 13S + \eta\beta) + 4nm e' \bigr) \lambda,$$
and $55\Sigma + 13S \le C(h_B/\ell^2 + (w+\eta)/\ell + S + 1 + \lambda_g)$ and $4 \le C$ give the bound $x_a$. In case (b) the sum along constant arcs gives $e \le 18\Sigma + 3R^2(S + 1 + \lambda_g) + 1$ and $|Z| \le (R+1)nm$; with $R + 1 \le 2R^2 \le CR^2$ the counting step gives $x_b$. $\square$

The admitted inputs of the local theory are thirteen statements. Some are properties of Wach modules: stability under $\Gamma$, comparison with $D_{\mathrm{cris}}$, level maps, bounded Frobenius poles, and freeness over the ring of letters in case A (Wach, *Représentations p-adiques potentiellement cristallines*; Berger, *Limites de représentations cristallines*). Others are lifting theorems for Wach modules, and statements of $p$-adic Hodge theory such as the two theorems above and the exactness of $D_{\mathrm{cris}}$ on strict sequences (Fontaine, *Représentations p-adiques semi-stables*, Exposé VIII of Astérisque 223). Two of them, [the split part](/entry/split-case-a-final/) and [the universal part](/entry/universal-general-statement-holds/) in case A, are proved from other inputs later in this chapter.

**Corollary 8.1.11 (Theorem B from the admitted inputs).** Let $C \ge 320$ and fix the period data and the Wach data at every prime. Assume the admitted inputs of the local theory and three further inputs on the jumps. Then for every prime $\ell$ and every pair $(K, L)$ good at level $1$ with $K$ in the maximal unramified extension of $\mathbb{Q}_\ell$, the conclusion of the local Theorem B holds with the constant $C$.

Lean: `Formalism.MainNotions.N.Ln17.frobenius_statement_of_fontaine` (also `Formalism.MainNotions.N.Ln17.stmt_holds`, the same statement with the arguments in another order, and `Formalism.MainNotions.N.Ln17.frobenius_statement_of_inputs`, the form with the inputs listed one by one).

*Proof.* The conclusion assumes $\ell \ge 11$, so $\ell \ne 2$ and we are in case A. Apply the local Theorem B. $\square$

**Remark 8.1.12 (Formalization).** The constant 320 is `Formalism.MainNotions.N.Ln17.C0` ([FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L17)). The admitted inputs are the conjunction `ArcLiftingSetup.admitted`, with thirteen parts; they are not unfolded here. The proof reads only twelve of them: the part `adm16` (the Bloch-Kato extension criterion) is never used, and inside `adm8` only the killer statements at levels and modulo are used, so the constant `Ckap` of `ArcLiftingSetup.Stmt` does not enter the conclusion. The three inputs on the jumps are `UsedJ` (`adm22`, `adm23` and `LetterConditionGlobal`), passed to the sum lemmas and not unfolded here. The name of the predicate `HidaSetting` has nothing to do with Hida theory. In the band condition the constant $C$ is the same as the constant of the bound, so a larger $C$ makes the band condition easier to satisfy. Part (a) asks that $\mathrm{up}$ changes at every step of $\mathbb{Z}/n$, so it is vacuous when $n$ is odd. The name `frobenius_statement_of_inputs` speaks of Frobenius, but the statement is Theorem B.
