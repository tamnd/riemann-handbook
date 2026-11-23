---
title: Towers of modular functions
decls:
  - GlobalTheory.FN.tower_exists
  - GlobalTheory.T.exists_modular_function_tower_algebraic_coefficients
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Towers of modular functions

The Kummer classes of this chapter live in the multiplicative group of a field of modular functions of all levels. This section defines that field, with its actions and its $q$-expansions, as one object: a tower of modular functions over an algebraically closed field $\Omega$. It then proves that a tower exists for each $\Omega$ that is an algebraic closure of $\mathbb{Q}$ and each embedding of $\Omega$ into $\mathbb{C}$, and that its $j$-function can be taken to be the classical one. The later sections of the chapter all start from a tower. The existence theorem is the input of [the theorem on towers in the modularity chapter](/entry/tower-ex/).

We use the [modular forms](/learn/automorphic-forms/#modular-forms) of Volume 1, the principal congruence subgroups $\Gamma(M)$, and the upper half plane $\mathcal{H} = \{z \in \mathbb{C} : \mathrm{Im}\, z > 0\}$. Let $\mathrm{GL}_2^+(\mathbb{Q})$ be the group of rational $2 \times 2$ matrices with positive determinant. It acts on $\mathcal{H}$ by Möbius maps $z \mapsto g z = (a z + b)/(c z + d)$.

**Definition 6.1.1 (Germs of meromorphic functions).** Let $\mathcal{M}$ be the ring of germs of functions $\mathbb{C} \to \mathbb{C}$ along the codiscrete filter of $\mathcal{H}$. Two functions have the same germ when they agree on $\mathcal{H}$ outside a discrete closed subset. A function holomorphic on $\mathcal{H}$ gives a germ, and so does a quotient of two such functions with a nonzero denominator.

So $\mathcal{M}$ contains the field of meromorphic functions on $\mathcal{H}$. Working with germs lets us divide without naming the poles.

**Definition 6.1.2 (Hahn series).** Let $\Omega$ be a field. The ring $\Omega((q^{\mathbb{Q}}))$ of Hahn series is the set of formal sums $\sum_{r \in \mathbb{Q}} a_r q^r$ with $a_r \in \Omega$ whose support $\{r : a_r \neq 0\}$ is well ordered. It contains the Laurent series in $q^{1/M}$ for every $M \geq 1$.

A modular function of level $M$ has a $q$-expansion in powers of $q^{1/M}$ at the cusp $\infty$. The Hahn series ring holds the expansions of all levels at once.

Fix a field $\Omega$ with $\mathbb{Q} \subseteq \Omega$ and a ring map $\varepsilon : \Omega \to \mathbb{C}$. For $x \in \mathbb{Q}$ let $e_\Omega(x) \in \Omega$ be an element with $\varepsilon(e_\Omega(x)) = e^{2\pi i x}$, when one exists. When $\Omega$ is algebraically closed it exists and is unique, and $e_\Omega(x)$ is a root of unity.

**Definition 6.1.3 (Tower of modular functions).** A *tower of modular functions* over $(\Omega, \varepsilon)$ is the following data. A field $K$ that is an $\Omega$-algebra. An $\Omega$-algebra map $\exp : K \to \Omega((q^{\mathbb{Q}}))$, the $q$-expansion. A right action $f \mapsto f|g$ of $\mathrm{GL}_2^+(\mathbb{Q})$ on $K$ by $\Omega$-algebra automorphisms, so $f|1 = f$ and $f|(gh) = (f|g)|h$. An action of $\mathrm{Gal}(\Omega/\mathbb{Q})$ on $K$ by ring automorphisms $f \mapsto s(f)$, with $\exp(s f) = s(\exp f)$ coefficient by coefficient. A ring map $\mathrm{an} : K \to \mathcal{M}$, the analytic germ. An element $j_K \in K$. These satisfy the following laws.

1. Constants: $\mathrm{an}(c) = \varepsilon(c)$ for $c \in \Omega$.
2. Möbius action: if $\mathrm{an}(f)$ is the germ of $\varphi$, then $\mathrm{an}(f|g)$ is the germ of $z \mapsto \varphi(g z)$.
3. Meromorphy: each $\mathrm{an}(f)$ is a quotient $a/b$ of functions holomorphic on $\mathcal{H}$ with $b \neq 0$.
4. Expansion: for each $f$ there are $\varphi$ with germ $\mathrm{an}(f)$ and $C \in \mathbb{R}$ such that $\varphi(z) = \sum_r \varepsilon(a_r) e^{2\pi i r z}$ for $\mathrm{Im}\, z > C$, where $\exp f = \sum_r a_r q^r$.
5. Level: each $f$ is fixed by $\Gamma(M)$ for some $M \geq 1$.
6. Upper triangular matrices: if $g = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix}$, then the coefficient of $q^{ra/d}$ in $\exp(f|g)$ is $e_\Omega(rb/d)$ times the coefficient of $q^r$ in $\exp f$.
7. Shimura reciprocity: let $f$ be fixed by $\Gamma(M)$, let $\zeta$ be a primitive $M$-th root of unity in $\Omega$, and let $s(\zeta) = \zeta^d$. If $\gamma = \begin{pmatrix} a & b \\ c & \delta \end{pmatrix}$ and $\gamma' = \begin{pmatrix} a' & b' \\ c' & \delta' \end{pmatrix}$ in $\mathrm{SL}_2(\mathbb{Z})$ satisfy $a' \equiv a$, $b' \equiv d b$, $d c' \equiv c$ and $\delta' \equiv \delta$ modulo $M$, then $s(f|\gamma) = s(f)|\gamma'$.
8. The $j$-function: $j_K$ is fixed by $\mathrm{SL}_2(\mathbb{Z})$, and $\exp j_K$ has integer coefficients, coefficient $1$ at $q^{-1}$, and no terms below $q^{-1}$. Its germ is the germ of a function holomorphic on $\mathcal{H}$.
9. Algebraicity: each $f \in K$ is algebraic over $\Omega(j_K)$.
10. Bounded denominators: for each $f$ there is $D \geq 1$ such that each coefficient of $\exp f$ times some power of $D$ is an algebraic integer.
11. Saturation: let $a, b$ be holomorphic on $\mathcal{H}$, $b \neq 0$, such that $a/b$ is invariant under $\Gamma(M)$ and is a root of a nonzero polynomial with coefficients in $\mathrm{an}(K)$. Then $a/b = \mathrm{an}(f)$ for some $f \in K$.
12. $q$-expansion principle: let $a$ be holomorphic on $\mathcal{H}$ and invariant under $\Gamma(M)$, and assume that for each $\gamma \in \mathrm{SL}_2(\mathbb{Z})$ the function $a(\gamma z)$ is a Laurent series in $e^{2\pi i z/M}$, bounded below, with coefficients in $\varepsilon(\Omega)$. Then $a = \mathrm{an}(f)$ for some $f \in K$.

The tower is *standard* if $\mathrm{an}(j_K)$ is the germ of the classical $j$-function $j = E_4^3/\Delta$.

The laws say that $K$ is the field of modular functions of all levels whose $q$-expansions at all cusps have coefficients in $\Omega$, viewed both analytically (through $\mathrm{an}$) and formally (through $\exp$). Law 7 is the Shimura reciprocity law for the action of $\mathrm{Gal}(\mathbb{Q}^{\mathrm{ab}}/\mathbb{Q})$ on modular functions (G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Chapter 6). It is the only link between the two actions, and the Kummer classes of later sections use it to compare Frobenius elements with Hecke operators.

**Example 6.1.4.** For $\Omega = \overline{\mathbb{Q}} \subset \mathbb{C}$, let $K$ be the field of meromorphic functions $f$ on $\mathcal{H}$ that are invariant under some $\Gamma(M)$, meromorphic at the cusps, and have $q$-expansions with algebraic coefficients at all cusps. Then $\exp$ is the expansion at $\infty$, $f|g = f \circ g$, and $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ acts on coefficients. This is the classical picture, and the theorem below builds it.

**Theorem 6.1.5 (A standard tower exists).** Let $\Omega$ be an algebraic closure of $\mathbb{Q}$ and let $\varepsilon : \Omega \to \mathbb{C}$ be a ring map. Then there is a standard tower of modular functions over $(\Omega, \varepsilon)$.

Lean: `GlobalTheory.FN.tower_exists` (also `GlobalTheory.T.exists_modular_function_tower_algebraic_coefficients`, a second name).

*Proof.* Let $E = \varepsilon(\Omega) \subseteq \mathbb{C}$. Let $R$ be the ring generated by the functions $f : \mathcal{H} \to \mathbb{C}$ that are fixed by some $\Gamma(N)$ and for which there is $w \geq 0$ such that, for each $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, the function $\Delta^w \cdot (f \circ \gamma)$ has a $q^{1/N}$-expansion with coefficients in $E$. A first lemma gives a field $K$ with an injective map $R \to K$ whose image generates $K$ as a field of fractions, with the $q$-expansion, the matrix action, the Galois action on coefficients and the germ map. The constants of $K$ are the image of the constant functions.

A second lemma gives an element $j_K$ of $K$ that comes from the classical function $j$. Its expansion is $q^{-1} + 744 + 196884 q + \cdots$ with integer coefficients, and $j$ is invariant under $\mathrm{SL}_2(\mathbb{Z})$. The function $j$ is holomorphic on $\mathcal{H}$ because it is a quotient of holomorphic forms by the nowhere vanishing $\Delta$.

Each law is then one lemma about $K$. The action is a right action because $(f \circ g) \circ h = f \circ (gh)$. The germ map sends a quotient of elements of $R$ to a quotient of holomorphic functions, and the $q$-expansions of elements of $R$ converge on a half plane. Each element of $R$ has a level, so each element of $K$ has one. The rule for upper triangular matrices is the substitution $q^r \mapsto e^{2\pi i r b/d} q^{ra/d}$. Shimura reciprocity holds for the generators of $R$, and so for $K$. Each element of $K$ is algebraic over $\Omega(j_K)$, since the field of modular functions of level $M$ is a finite extension of $\mathbb{C}(j)$ and the expansions are defined over $\Omega$. Bounded denominators, saturation and the $q$-expansion principle come from the same description of $R$.

Finally the tower is standard, since the germ of $j_K$ is the germ of $j$ by construction. $\square$

**Remark 6.1.6 (Formalization).** The statement with the second name is a wrapper that calls the first by `first | exact …` under `maxHeartbeats 1000000` ([ExistsModularFunctionTowerAlgebraicCoefficientsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsModularFunctionTowerAlgebraicCoefficientsStatement.lean#L12)). The element $e_\Omega(x)$ is defined with `Function.invFun`, so it is a junk value when $e^{2\pi i x}$ is not in the image of $\varepsilon$ ([ExpUpper.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExpUpper.lean#L39)). The holomorphy of the germ of $j_K$ is a law of the tower, yet several later statements repeat it as a hypothesis. The lemmas that check the laws for $K$ were read as statements and not unfolded.
