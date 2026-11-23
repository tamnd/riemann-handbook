---
title: Cup products of Kummer classes
decls:
  - GlobalTheory.T.hodgeTate_cup_kummer_classes_eq_dlog_determinant
  - GlobalTheory.K5.KummerCup.cup_kummer_dlog
  - GlobalTheory.T.cup_kummer_dlog_mod_primePow_levelL
  - GlobalTheory.K5.LevelDown.cup_kummer_dlog_mod
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cup products of Kummer classes

Let $x$ and $y$ be the Kummer characters of $p^n$-th roots of two units $u$ and $v$. Their cup product $x \cup y$ is a class of degree $2$. This section shows that, up to a bounded power of $p$, the class $x \cup y$ is a multiple of the single class $\lambda_\zeta \cup \lambda_q$, and that the multiple is the determinant $\alpha\beta' - \beta\alpha'$ of the logarithmic coordinates of $u$ and $v$, with a sign. In the language of differentials, $d\log u \wedge d\log v = (\alpha\beta' - \beta\alpha')\, d\log q \wedge d\log \zeta$, and the theorem says that the cup product of Kummer classes follows this rule. This is fact (A) in the proof of [the local edge congruence](/entry/edge-dlog/). The proof combines [the Kummer character formula](/entry/kummer-eq-dlog/) of the previous section with a lemma on cup products of $1$-cochains.

We keep the notation of the previous section.

**Definition 6.14.1 (Coboundaries of degree 2 modulo $p^k$).** Let $H \subseteq G$ be a subgroup and $k \geq 0$. A map $\xi : G \times G \to \Omega$ is a *coboundary modulo $p^k$ on $H$* if there is a map $w : G \to \Omega$ with the following properties:

1. $w(g)$ is integral for every $g \in G$;
2. $w$ is locally constant modulo $p^k$: for each $g \in G$ there is a finite set $S \subseteq \Omega$ with $w(h) \equiv w(g) \pmod{p^k}$ for every $h \in G$ that agrees with $g$ on $S$;
3. $\xi(g, h) \equiv g(w(h)) - w(gh) + w(g) \pmod{p^k}$ for all $g, h \in H$.

This is the finite level form of the statement that the class of $\xi$ in continuous cohomology of degree $2$ is zero. For two maps $x, y : G \to \mathbb{Z}/p^k$ the *cup product* is the $2$-cochain $(x \cup y)(g, h) = x(g)\, y(h)$, with the values read in $\{0, \ldots, p^k - 1\}$.

### The cup product lemma

We use the following lemma on cochains. Let $H \subseteq G$ be a subgroup and $n, c \geq 0$. Let $a, b, \lambda_\zeta, \lambda_q : G \to \mathbb{Z}/p^n$ be homomorphisms on $H$ that are locally constant on $G$. Let $A, B, A', B' \in \Omega$ be fixed by $H$, with $p^cA$, $p^cB$, $p^cA'$, $p^cB'$ integral. Assume that
$$
p^c a - p^c A\,\lambda_q - p^c B\,\lambda_\zeta \quad\text{and}\quad p^c b - p^c A'\lambda_q - p^c B'\lambda_\zeta
$$
are coboundaries modulo $p^n$ on $H$. Then the $2$-cochain
$$
(g, h) \mapsto p^{4c}\bigl(a(g)\,b(h) + (AB' - BA')\,\lambda_\zeta(g)\,\lambda_q(h)\bigr)
$$
is a coboundary modulo $p^n$ on $H$.

The idea is bilinearity. Up to coboundaries, $a \cup b$ equals $(A\lambda_q + B\lambda_\zeta) \cup (A'\lambda_q + B'\lambda_\zeta)$. For a homomorphism $\lambda$ and $p$ odd, $\lambda \cup \lambda$ is the coboundary of $-\lambda^2/2$, and $\lambda_q \cup \lambda_\zeta + \lambda_\zeta \cup \lambda_q$ is the coboundary of $-\lambda_\zeta\lambda_q$. So $a \cup b \equiv (BA' - AB')\,\lambda_\zeta \cup \lambda_q$. The powers of $p$ clear the denominators of $A$, $B$, $A'$, $B'$ and of the factor $2$.

### Units with a power of $\zeta_n - 1$

**Theorem 6.14.2 (Cup products at the level of the units).** Let $p$ be an odd prime. There is $c \geq 0$ with the following property. Let $\Omega$ be a closure of $\mathcal{O}$ with a tower, $n \geq 1$, and $\iota$ an embedding of $\mathcal{O}_n$. Let $k, l \in \mathbb{Z}$. Let $w, w'$ be units of $\mathcal{O}_n$ with logarithmic coordinates $(\alpha, \beta)$ and $(\alpha', \beta')$. Let $r, s \in \Omega$ with
$$
r^{p^n} = (\zeta_n - 1)^k\,\iota(w), \qquad s^{p^n} = (\zeta_n - 1)^l\,\iota(w').
$$
Let $a$, $b$, $\lambda_\zeta$, $\lambda_q$ be Kummer characters of $r$, $s$, $\zeta_{2n}$, $q_{2n}$ on $G_n$. Put
$$
f = \alpha\bigl(lX + (X - 1)\beta'\bigr) - \bigl(kX + (X - 1)\beta\bigr)\alpha' \in \mathcal{O}_n .
$$
Then
$$
(g, h) \mapsto p^c a(g)\,b(h) + p^c\,\frac{\iota(f)}{\zeta_n - 1}\,\lambda_\zeta(g)\,\lambda_q(h)
$$
is a coboundary modulo $p^n$ on $G_n$.

Lean: `GlobalTheory.K5.KummerCup.cup_kummer_dlog` (also `GlobalTheory.T.hodgeTate_cup_kummer_classes_eq_dlog_determinant`, a second name).

The element $\iota(f)/(\zeta_n - 1)$ equals $AB' - BA'$ with
$$
A = \iota(\alpha), \quad B = \iota(\beta) + \frac{k\,\zeta_n}{\zeta_n - 1}, \quad A' = \iota(\alpha'), \quad B' = \iota(\beta') + \frac{l\,\zeta_n}{\zeta_n - 1}.
$$
These are the logarithmic coordinates of the two radicands, including the factors $(\zeta_n - 1)^k$ and $(\zeta_n - 1)^l$.

*Proof.* Let $c_1$ be the constant of [the Kummer character formula](/entry/kummer-eq-dlog/). We show that $c = 4(c_1 + 1)$ works. By that theorem, $p^{c_1}a - p^{c_1}A\lambda_q - p^{c_1}B\lambda_\zeta$ is a coboundary modulo $p^n$ on $G_n$, and the same holds for $b$ with $A'$, $B'$. Multiply both by $p$. The elements $A$, $B$, $A'$, $B'$ are fixed by $G_n$, since they lie in the image of $\mathcal{O}_n$ and in the field generated by $\zeta_n$. The element $p/(\zeta_n - 1)$ is integral, so $p^{c_1+1}A$, $p^{c_1+1}B$, $p^{c_1+1}A'$, $p^{c_1+1}B'$ are integral.

The cup product lemma needs homomorphisms on $G_n$ that are locally constant on all of $G$. A Kummer character is a homomorphism on $G_n$: if $g(r) = \zeta_n^{a(g)}r$ and $h(r) = \zeta_n^{a(h)}r$, then $gh(r) = \zeta_n^{a(g) + a(h)}r$ since $g$ fixes $\zeta_n$. Replace $a$, $b$, $\lambda_\zeta$, $\lambda_q$ by the maps that agree with them on $G_n$ and are $0$ outside $G_n$. These maps are locally constant: membership in $G_n$ and the values on $G_n$ are fixed by the action on the finite set $\{\zeta_n, q_n, r, s, \zeta_{2n}, q_{2n}\}$. Nothing changes on $G_n$. The cup product lemma with the constant $c_1 + 1$ now gives the claim, since $AB' - BA' = \iota(f)/(\zeta_n - 1)$ by the definition of $f$. $\square$

### Units at level $L$, characters at level $n$

The edge congruence needs the cup product for units of $\mathcal{O}_L$ and roots of order $p^n$ with $n \leq L$. The characters are then taken on $G_L$, and the basic characters are those of $\zeta_{L+n}$ and $q_{L+n}$.

**Theorem 6.14.3 (Cup products of Kummer classes).** Let $p$ be an odd prime. There is $c \geq 0$ with the following property. Let $\Omega$ be a closure of $\mathcal{O}$ with a tower, $1 \leq n \leq L$, and $\iota$ an embedding of $\mathcal{O}_L$. Let $u, v$ be units of $\mathcal{O}_L$ with logarithmic coordinates $(\alpha, \beta)$ and $(\alpha', \beta')$. Let $r, s \in \Omega$ with $r^{p^n} = \iota(u)$ and $s^{p^n} = \iota(v)$. Let $a$, $b$, $\lambda_\zeta$, $\lambda_q$ be Kummer characters, with values in $\mathbb{Z}/p^n$, of $r$, $s$, $\zeta_{L+n}$, $q_{L+n}$ on $G_L$. Then
$$
(g, h) \mapsto p^c a(g)\,b(h) + p^c\,\iota(\alpha\beta' - \beta\alpha')\,\lambda_\zeta(g)\,\lambda_q(h)
$$
is a coboundary modulo $p^n$ on $G_L$.

Lean: `GlobalTheory.K5.LevelDown.cup_kummer_dlog_mod` (also `GlobalTheory.T.cup_kummer_dlog_mod_primePow_levelL`, a second name).

*Proof.* Take $c$ from the previous theorem. Choose $R, S \in \Omega$ with $R^{p^{L-n}} = r$ and $S^{p^{L-n}} = s$. Then $R^{p^L} = \iota(u)$ and $S^{p^L} = \iota(v)$. Choose Kummer characters $a_L$, $b_L$, $z_L$, $q_L'$ with values in $\mathbb{Z}/p^L$ of $R$, $S$, $\zeta_{2L}$, $q_{2L}$ on $G_L$; they exist since $G_L$ fixes $\iota(u)$, $\iota(v)$, $\zeta_L$ and $q_L$. Apply the previous theorem at level $L$ with $k = l = 0$. Then $f = (X - 1)(\alpha\beta' - \beta\alpha')$ and $\iota(f)/(\zeta_L - 1) = \iota(\alpha\beta' - \beta\alpha')$. So
$$
(g, h) \mapsto p^c a_L(g)\,b_L(h) + p^c\,\iota(\alpha\beta' - \beta\alpha')\, z_L(g)\, q_L'(h)
$$
is a coboundary modulo $p^L$ on $G_L$.

Now compare the characters. For $g \in G_L$ we have $g(R) = \zeta_L^{a_L(g)}R$. Raise to the power $p^{L-n}$: since $\zeta_L^{p^{L-n}} = \zeta_n$, this gives $g(r) = \zeta_n^{a_L(g)} r$. So $a(g) \equiv a_L(g) \pmod{p^n}$. In the same way $b \equiv b_L$, and, since $\zeta_{2L}^{p^{L-n}} = \zeta_{L+n}$ and $q_{2L}^{p^{L-n}} = q_{L+n}$, also $\lambda_\zeta \equiv z_L$ and $\lambda_q \equiv q_L'$ modulo $p^n$. The element $\iota(\alpha\beta' - \beta\alpha')$ is integral. A congruence modulo $p^L$ implies the congruence modulo $p^n$, and a cochain that is locally constant modulo $p^L$ is locally constant modulo $p^n$. Replacing each character by its congruent one changes the $2$-cochain by a multiple of $p^n$. This gives the claim. $\square$

**Remark 6.14.4.** The theorem says that, up to a bounded power of $p$ and a coboundary, the cup product of the Kummer classes of two units is computed from $d\log u \wedge d\log v$. The bound does not depend on $n$, $L$, the tower or the units.

**Remark 6.14.5 (Formalization).** Both second names are wrappers of the form `first | exact @… | …`. The cup product lemma is `GlobalTheory.T.kummer_cochain_cup_product_congruence`, a wrapper of `GlobalTheory.CuspCup.cup_congruence`. It is not among the declarations of this chapter; we read it as a statement, and the sketch of its idea above is ours. In the level $L$ theorem the result at level $L$ is used only with $k = l = 0$ ([CupKummerDlogModPrimePowLevelL.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/CupKummerDlogModPrimePowLevelL.lean#L110)), so the factors $(\zeta_n - 1)^k$ play no role in the rest of the chapter.
