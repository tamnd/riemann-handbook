---
title: Hecke eigenvalues and Frobenius at tame primes
decls:
  - UpperTheory.V.Z.Kato.Nb.sEs
  - UpperTheory.V.Z.Kato.Nb.sEuler
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke eigenvalues and Frobenius at tame primes

An Euler system needs a norm relation at each tame prime $p$: the sum of the classes at level $p$ is the class at level $1$ times the Euler factor of the representation at $p$. The norm relation for Kato's zeta classes is proved in Section 6, in the form that the [gluing of zeta classes](/entry/k4-top/) uses. Its Euler factor comes from Hecke operators, and this section relates these operators to Frobenius elements. First, the Eichler-Shimura relation on Kummer modules writes the Hecke operator $T_p$ through a Frobenius element. Second, this relation identifies the Hecke eigenvalues on the projected classes with the trace and the determinant of Frobenius for the twist of $W$, and so it gives the Euler factor $\det(W(\sigma) - 1)$ modulo powers of $l$.

### Setting

We keep the notation of Section 4. So $l$ is a prime, $\Omega$ is an algebraic closure of $\mathbb{Q}$ with $G_{\mathbb{Q}} = \mathrm{Gal}(\Omega/\mathbb{Q})$, $X$ is a tower of modular functions over $\Omega$ with function field $K$, and $\varepsilon$ is the [[cyclotomic character|XSGB5K2KEG]]. For a level $N \geq 1$ and a weight $w$, let $\mathcal{K}_w(N)$ be the Kummer module of $X$ of level $N$ and weight $w$. It is spanned by the Kummer classes $b$, which are functions $u \mapsto b(u)$ from $\mathbb{Z}_l^2$ to the $l$-adic completion of $K^\times$. The group $G_{\mathbb{Q}}$ acts on $\mathcal{K}_w(N)$ by $b \mapsto s \cdot b$, the matrices of $\mathrm{GL}_2^+(\mathbb{Q})$ act by $b \mapsto b|\gamma$, and for a prime $q \nmid lN$ there are the Hecke operator $T_q$ and the diamond operator $\langle q\rangle$.

For a valuation ring $B$ of $\Omega$ over a place $v$ with prime norm $q$, a *Frobenius at $q$ for $B$* is an element $\sigma \in G_{\mathbb{Q}}$ that fixes $B$ and induces the $q$-th power map on its residue field, as in the [Kummer congruence](/entry/eichler-shimura-kummer-function-uniform-exceptional-primes/). A *diamond matrix for $q$ modulo $M$* is $\gamma \in \mathrm{SL}_2(\mathbb{Z})$ with $\gamma_{12} \equiv \gamma_{21} \equiv 0$ and $\gamma_{22} \equiv q$ modulo $M$.

For a representation $W$ in normal form, a newform $g$ of weight $2e+1$ and the data of Section 4, let $\rho$ be the twist of $W$ that is used for zeta classes. For a prime $p$ and $a, \delta \in \overline{\mathbb{Q}}_l$ put
$$
\mathrm{eul}_p(a, \delta) = 1 - a\, p^{-(e+1)} + \delta\, p^{-2}.
$$

### The Eichler-Shimura relation

**Theorem 8.5.1 (Eichler-Shimura relation on Kummer modules).** Let $l$ be an odd prime, $N \geq 1$ and $w \in \mathbb{N}$. There is a finite set $S_0$ of primes with the following property. Let $v$ be a place with prime norm $q \notin S_0$, let $B$ be a valuation ring over $v$ and $\sigma$ a Frobenius at $q$ for $B$. Then for each $b \in \mathcal{K}_w(N)$
$$
T_q b = \sigma \cdot b + q^{w+1}\, \langle q\rangle\bigl(\sigma^{-1} \cdot b\bigr).
$$

Lean: `UpperTheory.V.Z.Kato.Nb.sEs`.

*Proof.* We use four facts. The first is the level statement: each Kummer class $b$ of weight $w$ is locally constant modulo $l^n$, it is homogeneous of degree $w$, and for each $n$ and $u$ the element $4b(u)$ is represented modulo $l^n$ by a modular unit $F$ of level $6lN\,l^k$ for some $k \geq n$. The second is that a Frobenius $\sigma$ at $q \neq l$ is a Frobenius for the valuation and satisfies $\varepsilon(\sigma) = q$. The third is the coset decomposition
$$
T_q b = \sum_{j=0}^{q-1} b\Big|\begin{pmatrix} 1 & jM \\ 0 & q\end{pmatrix} + b\Big|\Bigl(\gamma\begin{pmatrix} q & 0 \\ 0 & 1\end{pmatrix}\Bigr)
$$
for a diamond matrix $\gamma$ for $q$ modulo $M$, together with $\langle q\rangle(s \cdot b) = s \cdot (b|\gamma)$. The fourth is the [Kummer congruence](/entry/eichler-shimura-kummer-function-uniform-exceptional-primes/) for $M_0 = 6lN$, which gives a finite set $S$ of primes.

Put $S_0 = S \cup \{\text{primes dividing } 6lN\}$. Then $q \notin S_0$ is prime to $6lN$, so $q \neq l$. Both sides of the relation are linear in $b$, so it is enough to prove it for a Kummer class $b$. Two elements of the $l$-adic completion are equal if they are equal modulo $l^n$ for each $n$. Fix $n$ and $u$, and let $F$ represent $4b(u)$ modulo $l^n$. The Kummer congruence for $F$ says that $N_q(F)$ times $F|\gamma\,\mathrm{diag}(q, 1)$ equals $\sigma(F)$ times $(\sigma^{-1}(F|\gamma))^q$, up to an $l^n$-th power. In additive notation for the Kummer classes, the left side is $4\,T_q b(u)$ by the coset decomposition. On the right side, the factor $\sigma(F)$ gives $4\,\sigma\cdot b(u)$, and the factor $(\sigma^{-1}(F|\gamma))^q$ gives $4q\,\langle q\rangle(\sigma^{-1}\cdot b)(u)$ with the twist of weight $w$, which contributes $q^w$, because $\varepsilon(\sigma) = q$. Since $4$ is a unit in $\mathbb{Z}_l$ for $l$ odd, this gives the relation modulo $l^n$. $\square$

### Hecke eigenvalues and Frobenius

**Theorem 8.5.2 (Frobenius traces of the twist).** Let $e \geq 1$, let $l \nmid N$, let $W$ be in normal form for $(e, S, A)$ with entries in $\mathcal{O}$, and let the data be admissible at $x \in \mathbb{Z}/N$. There is a finite set $S' \supseteq S$ of places with the following property. For each place $w \notin S'$, the norm $Nw$ is a prime prime to $lNcd$, and there are $a, \delta \in \mathcal{O}$ such that:

1. $\mathrm{pr}(T_{Nw}\, b) = a\, \mathrm{pr}(b)$ and $\mathrm{pr}(\langle Nw\rangle b) = \delta\, \mathrm{pr}(b)$ for each $b \in \mathcal{K}_{2e-1}(N)$;
2. for each valuation ring $B$ over $w$ and each Frobenius $\sigma$ at $Nw$ for $B$, $\varepsilon(\sigma) = Nw$, $\mathrm{tr}\,\rho(\sigma) = a$ and $\det\rho(\sigma) = (Nw)^{2e}\delta$.

Lean: `UpperTheory.V.Z.Kato.Nb.sEuler`.

*Proof.* Let $S_0$ be the set of the Eichler-Shimura relation for $N$ and weight $2e - 1$. Let $S'$ be the union of $S$, the places with norm in $S_0$ and the places with norm dividing $lNcd$. For $w \notin S'$ put $q = Nw$. Then $q$ is prime to $lNcd$.

First assume that $\mathrm{pr}(b) \neq 0$ for some $b \in \mathcal{K}_{2e-1}(N)$. The diamond operators act on the projected classes through a character $\delta$ of $(\mathbb{Z}/N)^\times$, and the Hecke operator $T_q$ acts by the eigenvalue $a = a_q(g)$ of the newform. The image of $\mathrm{pr}$ is a nonzero subspace of $\overline{\mathbb{Q}}_l^2$, and it is stable under $\rho$ by Galois equivariance. Since $W$ is irreducible on the subgroup of the normal form, this image is all of $\overline{\mathbb{Q}}_l^2$. Put $\chi = \varepsilon^{2e}\,\delta$. Project the Eichler-Shimura relation by $\mathrm{pr}$. Since $\mathrm{pr}$ is Galois equivariant and the image spans, it gives
$$
\rho(\sigma) - a + \chi(\sigma)\,\rho(\sigma)^{-1} = 0,
$$
so $\rho(\sigma)^2 - a\rho(\sigma) + \chi(\sigma) = 0$ for each Frobenius $\sigma$ at $q$. Both $\rho$ and $\chi$ are continuous, and $\rho$ is not scalar, again by irreducibility. By the [[Galois representation|JQEYEQJY2G]] form of the Chebotarev density theorem, a continuous two-dimensional representation whose Frobenius elements satisfy such quadratic relations with a continuous character $\chi$ outside a finite set has determinant $\chi$. So $\det\rho(\sigma) = q^{2e}\delta(q)$, and the quadratic relation for a $2 \times 2$ matrix with this determinant gives $\mathrm{tr}\,\rho(\sigma) = a$.

Now assume that $\mathrm{pr}$ is zero on $\mathcal{K}_{2e-1}(N)$. Fix one Frobenius $\sigma_0$ at $q$ and put $a = \mathrm{tr}\,\rho(\sigma_0)$ and $\delta = q^{-2e}\det\rho(\sigma_0)$. Clause 1 holds since both sides are zero. Since $W$ is unramified at $w \notin S$, all Frobenius elements at $q$ have conjugate images under $W$ and the same cyclotomic character, so clause 2 holds for each $\sigma$.

In both cases $\varepsilon(\sigma) = q$ because $q \neq l$. The entries of $\rho$ lie in $\mathcal{O}$, so $a \in \mathcal{O}$. Since $q$ is prime to $l$, $q^{-1} \in \mathcal{O}$, and $\delta = q^{-2e}\det\rho(\sigma)$ lies in $\mathcal{O}$. $\square$

When $l^n$ divides $p - 1$, the element $\mathrm{eul}_p(a, \delta)$ lies in $\mathcal{O}$ and is congruent modulo $l^n$ to $\det(W(\sigma) - 1)$ for each Frobenius $\sigma$ at $p$. Indeed $\det(W(\sigma) - 1) = 1 - \mathrm{tr}\,W(\sigma) + \det W(\sigma)$, and $p \equiv 1 \bmod l^n$ makes the powers of $p$ in $\mathrm{eul}_p$ congruent to $1$.

**Remark 8.5.3 (Formalization).** The Eichler-Shimura relation takes the hypothesis that $l$ is odd, and the proof uses it only to make $4$ a unit ([EsOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/EsOf.lean#L116)). The holomorphy of the $j$-function is not a hypothesis there: it is read off the tower ([EsOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/EsOf.lean#L21)), since every tower carries it as a field ([ExpUpper.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExpUpper.lean#L89)). So the holomorphy hypotheses of the coefficient law and of the Hodge-Tate law in Section 4 are redundant. In the Frobenius traces theorem, the case where the projection is zero is handled by a separate branch, in which clause 1 holds trivially ([FrobeniusConjugateInertia.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/FrobeniusConjugateInertia.lean#L162)). The Euler factor $\mathrm{eul}_p$ uses the factors $p^{-(e+1)}$ and $p^{-2}$, which are congruent to $1$ only modulo $l^n$ ([SPushPsi.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/SPushPsi.lean#L19)).
