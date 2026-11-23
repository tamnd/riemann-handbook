---
title: The odd block supply
decls:
  - GlobalTheory.MinorShiftJet.window_letterDet
  - GlobalTheory.oddBlock_supply
  - GlobalTheory.T.oddLevelBlock_bound_attained
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The odd block supply

This section proves the supply of odd blocks. Let $X$ be an alternating row datum with $\ell \geq 5$ and $n \geq 1$, let $(g, a)$ be big and let $i < d$ be odd. Then the block of jets between the type $a$ on side $g$ and the type $a + i$ on side $1 - g$, with exponents $\ell^i y$ and $y$, has a value of valuation at most an explicit bound for $y = 0$ and for at least one $y$ in every interval of length $S_0(n)$. The proof puts together the [normal form of the main term](/entry/cm-theta-values/depth-valuations/#main-terms-at-odd-levels) and the [window bounds for block jets](/entry/cm-theta-values/depth-valuations/#binomial-values-and-window-bounds). The supply is one of the three block supplies in the [depth bound at good places](/entry/cm-theta-values/depth-valuations/#depth-bounds-at-good-places), through the block bound of the [packages of row data](/entry/cm-theta-values/depth-valuations/#row-data-and-packages-at-good-primes). It is used in the same way in the content bounds at inert primes and at places where Frobenius acts as complex conjugation.

### Blocks and their values

We keep the row data of the section on main terms, with the notation $S_0$, $b(n_0, n, y)$, $\gamma$ and $[P, G]$ of the previous section. The valuation $v$ has $v(\ell) = 1$, and the letters of side $g$ form the set $I_g$. Let $I = I_0 \sqcup I_1$ be the set of all letters.

For $N \geq 1$ take variables $x_{\rho, w}$ for rows $\rho < N$ and letters $w \in I$. For a series $F$ in the variables $x_w$, $w \in I$, let $F^{(\rho)}$ be its copy in the variables of row $\rho$. Let $t$ be standard coordinates for a pair of systems $S_0, S_1$ on the charts $G_0, G_1$. A series $F$ in the variables $x_w$ is an *integral germ* for $t$ if $F = \gamma\bigl((t_{w})_{w \in I}\bigr)$ for a series $\gamma$ with integral coefficients, where $t_w$ for $w = (g, x)$ is the coordinate $t_{g,x}$ in the variables of side $g$. For a polynomial $P$ in the $x_{\rho, w}$ and integral germs $\mathrm{gr}_0, \dots, \mathrm{gr}_{N-1}$, the *value* at $(g, a, a')$ is
$$\mathrm{Val}(P, \mathrm{gr}) = \Bigl[P, \prod_{\rho < N} \mathrm{gr}_\rho^{(\rho)} \exp\bigl(h(g, a, a')^{(\rho)}\bigr)\Bigr].$$
The germs $\mathrm{gr}_\rho$ allow integral changes of coordinates on each row. The block bound of the packages bounds a valuation $\nu$ by sums of values of blocks. The supply gives blocks whose values have valuation at most an explicit number, so $\nu$ is at most a sum of these numbers.

For an injective map $p$ from $\{0, \dots, n - 1\}$ to $I_g$ let $\Delta_p = \det(x_{\rho, p(c)})_{\rho, c < n}$ be the determinant of the $n \times n$ minor on the letters $p(0), \dots, p(n-1)$. The *block bound* is
$$\beta(y) = 0 \ \text{ if } y = 0, \qquad \beta(y) = b(n, n, y) + \frac{(i + 1)\, m\, (\ell^i + 1)\, y}{\ell - 1} \ \text{ if } y \geq 1,$$
where $m = j + j'$. A set $Y$ of integers $y \geq 0$ has *windows of length $S$* if $0 \in Y$ and every interval $[Y_0, Y_0 + S)$ with $Y_0 \geq 0$ meets $Y$.

A *flag* of $X$ is, for each $(g, a)$, an enumeration $\mathrm{en}_{g,a}$ of the letters of $I_g$ of type $a$, without repetitions. When $(g, a)$ is big there are $n + j \geq n$ of them, and $\mathrm{en}_{g,a}$ restricted to the first $n$ indices is an injective map $p_{g,a}$ as above.

### Windows for minors

**Lemma 4.16.1 (shifted types).** Let $X$ be alternating, let $(g, a)$ be big and let $i$ be odd. Then $(1 - g, a + i)$ is big.

*Proof.* The modulus $d$ is even, so the parity of the representative of $a + i$ in $[0, d)$ is that of $a + i$, which is opposite to that of $a$. If $g = 0$, then $a$ is even, $a + i$ is odd, so $(0, a + i)$ is not big and $(1, a + i)$ is big. If $g = 1$, then $(0, a)$ is not big, so $a$ is odd and $a + i$ is even, and $(0, a + i)$ is big. $\square$

**Theorem 4.16.2 (windows for minors).** Let $X$ be an alternating row datum with $\ell \geq 5$ and $n \geq 1$. Let $(g, a)$ be big, let $i < d$ be odd, and let $p : \{0, \dots, n-1\} \to I_g$ and $p' : \{0, \dots, n-1\} \to I_{1-g}$ be injective, with all letters $p(c)$ of type $a$ and all letters $p'(c)$ of type $a + i$. Let $Y$ be the set of $y \geq 0$ for which there are systems with standard coordinates $t$ and integral germs $\mathrm{gr}_0, \dots, \mathrm{gr}_{n-1}$ for $t$ such that
$$v\Bigl(\mathrm{Val}\bigl(\Delta_p^{\ell^i y}\, \Delta_{p'}^{y}, \mathrm{gr}\bigr)\Bigr) \leq \beta(y),$$
the value taken at $(g, a, a + i)$. Then $Y$ has windows of length $S_0(n)$.

Lean: `GlobalTheory.MinorShiftJet.window_letterDet`.

*Proof.* Step 1 (normal form). Let $U_b$ be the unit vector at $p(b)$ and $U'_b$ the unit vector at $p'(b)$. The family $U$ has integral entries and its transpose is an integral right inverse, since $p$ is injective. So $U$ is saturated, and it is supported on letters of type $a$; the same holds for $U'$ with the type $a + i$. The first of the main term lemmas gives a normal form $n_0, e, v', \Phi$ of $(U, U')$ at $(g, a, i)$ with the curve clause. In particular $n_0 \leq n$ and $n \leq n_0 + (i + 1) j' + j$. Since $(i + 1) m = (i + 1) j' + j + i j$, this gives $n - n_0 \leq (i + 1) m$.

Step 2 (row hypothesis). A lemma on the main term, which we use through its statement, gives from the normal form a series $h_1$ in $2 n_0^2$ variables with conditions (H1) and (H2) of the previous section, such that the row series built from $h(g, a, a + i)$, $e$ and $v'$ restricts to $h_P$ on the first $n_0$ rows and columns.

Step 3 (block reduction). A second lemma turns the value into a block jet. It gives systems with standard coordinates $t$ and series $h^r_\rho, t_\rho, t'_\rho$ for $\rho < n$ that satisfy the block hypothesis of the previous section for $h_1$, such that for every $y$ there are integral germs $\mathrm{gr}$ for $t$ with
$$v\Bigl(\mathrm{Val}\bigl(\Delta_p^{\ell^i y} \Delta_{p'}^{y}, \mathrm{gr}\bigr)\Bigr) \leq v\bigl(J(y)\bigr),$$
where $J(y)$ is the block jet of the previous section with $n$ rows. Its proof completes the rows of $A$ in $e = A U$ to an integral matrix with integral inverse, inverts $Y$ in $v' = Y U'$ over the integers, and uses that a linear change of the letters by a matrix $B$ multiplies the minor by $\det B$. An integral factor can only raise the valuation.

Step 4 (the bound for one $y$). We claim that $y \in Y$ whenever $y = 0$ or $v(J(y)) \leq \beta(y)$ with $y \geq 1$. For $y \geq 1$ this is Step 3. For $y = 0$, the polynomial is $1$ and every factor $F_\rho$ is $1$, so $J(0)$ is the constant term of $\prod_\rho \exp(h^r_\rho)$, which is $1$. So $v(J(0)) = 0 = \beta(0)$. In particular $0 \in Y$.

Step 5 (windows when $n_0 = 0$). Let $Y_0 \geq 0$ and take $y = Y_0$. Since $S_0(n) \geq 1$, $y$ lies in $[Y_0, Y_0 + S_0(n))$. The block value lemma gives $J(y) = ((\ell^i y)!\, y!)^n\, \Lambda(y)$, and $\Lambda(y) = 1$ because $n_0 = 0$. Now $v(1) = 0 \leq b(0, n, y) = n(\log_\ell n + 1)$. The content bound of the previous section gives
$$v(J(y)) \leq b(n, n, y) + \frac{n (\ell^i + 1) y}{\ell - 1} \leq \beta(y),$$
using $n \leq (i + 1) m$ from Step 1. By Step 4, $y \in Y$.

Step 6 (windows when $n_0 \geq 1$). The window part of the content and window theorem applies, with $n - n_0 \leq (i + 1) m$, the block hypothesis, (H1) and (H2). It gives $y \in [Y_0, Y_0 + S_0(n_0))$ with $v(J(y)) \leq \beta(y)$ if $y \geq 1$. Since $n_0 \leq n$, $\ell > 1$ and $\log_\ell$ is increasing, $S_0(n_0) \leq S_0(n)$. So $y$ lies in $[Y_0, Y_0 + S_0(n))$, and $y \in Y$ by Step 4. $\square$

The proof does not use the level one clause of the normal form, nor the second part of the main term lemma of Step 2.

### The supply

**Theorem 4.16.3 (odd block supply).** Let $X$ be an alternating row datum with a flag, $\ell \geq 5$ and $n \geq 1$. Let $(g, a)$ be big and let $i < d$ be odd. Let $Y$ be the set of $y \geq 0$ for which there are systems with standard coordinates $t$ and integral germs $\mathrm{gr}_0, \dots, \mathrm{gr}_{n-1}$ for $t$ such that
$$v\Bigl(\mathrm{Val}\bigl(\Delta_{p_{g,a}}^{\ell^i y}\, \Delta_{p_{1-g, a+i}}^{y}, \mathrm{gr}\bigr)\Bigr) \leq \beta(y),$$
the value taken at $(g, a, a + i)$. Then $Y$ has windows of length $S_0(n)$.

Lean: `GlobalTheory.oddBlock_supply` (also `GlobalTheory.T.oddLevelBlock_bound_attained`, a second name).

*Proof.* Since $(g, a)$ is big, $I_g$ has $n + j \geq n$ letters of type $a$, so $p_{g,a}$ is defined. By the lemma on shifted types, $(1 - g, a + i)$ is big, so $I_{1-g}$ has $n + j \geq n$ letters of type $a + i$ and $p_{1-g, a+i}$ is defined. Both maps are injective, as restrictions of enumerations without repetitions, and their letters have the types $a$ and $a + i$. The determinant of the leading $n \times n$ minor of the matrix $(x_{\rho, \mathrm{en}_{g,a}(c)})$ is $\Delta_{p_{g,a}}$, and the same holds on side $1 - g$. The theorem on windows for minors, applied to $p = p_{g,a}$ and $p' = p_{1-g, a+i}$, gives the claim. $\square$

For $y \geq 1$ the bound reads
$$\beta(y) = y \Bigl( n\bigl((\ell^i + 1)\gamma - 1\bigr) + \frac{(i + 1) m (\ell^i + 1)}{\ell - 1} \Bigr) + n(\log_\ell n + 1).$$
Its slope in $y$ is about $n \ell^{i-1}$ when $m$ is small compared with $n$, against the exponent $\ell^i y + y$ of the block. The windows have a length that depends on $n$, $i$ and $\ell$ only, so the bound holds along a set of $y$ of positive density.

**Remark 4.16.4 (Formalization).** The theorem on minors is at [OddLevelBlockBoundAttained.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/OddLevelBlockBoundAttained.lean#L89), the lemma on shifted types at line 24 and the supply at line 155; the second name is in [OddLevelBlockBoundAttainedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/OddLevelBlockBoundAttainedStatement.lean#L8). The supply is stated twice, as a conjunction. The first half uses the flags of [ContentLargeFromSupplies.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentLargeFromSupplies.lean#L72), built on a rank function at line 15; the second uses a second copy of the same flags and rank in [ContentZeroAt.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentZeroAt.lean#L78), with the rank at line 21. The two halves of the proof, lines 157 to 166 and 167 to 176, are the same text. The three users, in GoodPlaceDepthBoundProof.lean line 61, ComplexConjFrobeniusDepthContentBoundProof.lean line 362 and InertPrimeDepthContentBoundProof.lean line 212, take only the second half. The block bound and the windows are defined in ContentZeroAt.lean at lines 11 and 16, and again in ValuationChoiceHypothesis.lean at lines 34 and 42. The second names of the supply, of the main term lemma of Step 2 and of the block value lemma are relays that try three tactics in turn under a raised heartbeat limit. The proof of the theorem on minors discards the level one clause at line 99, and the block reduction lemma is in BlockOfNormalForm.lean at line 317. We did not unfold the row series of Step 2 or the restriction map of the block hypothesis.

## Notes and references

The chapter feeds the [depth bounds of a record](/entry/leaf-depth-all-record/), the [lattices at the leaves](/entry/leaves-sup-span-data/) and the [six rows at a member](/entry/six-rows-at-member-alt/) in Volume 15, and through them Branch 2 of [the unitary hypotheses](/proof/unitary-hypotheses/).

Sections 1 and 2 follow Lubin and Tate. They prove that formal groups of height one over the integers of $\mathbb{C}_p$ are all isomorphic to $\hat{\mathbb{G}}_m$; here the isomorphism is built from a tower of torsion points, without the classification of formal group laws. The multiplicative chart at a split prime comes from the ordinary reduction of a CM curve, as in Silverman. Sections 3, 8 and 9 build measures in the manner of Katz, with Mahler's theorem in the form "a measure on $\mathbb{Z}_q$ of norm at most $1$ is a series in $T$ with integral coefficients"; the theta functions are those of Mumford. The biextensions of Section 13 are those of Grothendieck and Mumford, used here only through a nondegenerate pairing modulo the maximal ideal. The Cayley identity of Section 15, $\det(\partial)\det(x)^{s+1} = (s + 1)\cdots(s + n_0)\det(x)^s$, is classical; the pairing form $\langle \Delta^x, \Delta^x \rangle = \mathrm{cap}(n_0, x)$ follows from it, and it is a special case of the Capelli identity. The binomial windows are a finite form of the fact that a Mahler series with a unit leading coefficient and coefficients tending to $0$ cannot vanish modulo the maximal ideal on $S$ consecutive integers. The rest of the chapter, the row data, the main terms and the lattice chains, has no published source that we know of.

- J. Lubin and J. Tate, Formal complex multiplication in local fields, *Ann. of Math.* 81 (1965), pages 380 to 387.
- J. Lubin and J. Tate, Formal moduli for one-parameter formal Lie groups, *Bull. Soc. Math. France* 94 (1966), pages 49 to 59.
- M. Lazard, Sur les groupes de Lie formels à un paramètre, *Bull. Soc. Math. France* 83 (1955), pages 251 to 274.
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, Chapter IV (formal groups) and Chapter VII (elliptic curves over local fields).
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II (complex multiplication).
- N. M. Katz, p-adic interpolation of real analytic Eisenstein series, *Ann. of Math.* 104 (1976), pages 459 to 571.
- N. M. Katz, p-adic L-functions for CM fields, *Invent. Math.* 49 (1978), pages 199 to 297.
- K. Mahler, An interpolation series for continuous functions of a p-adic variable, *J. reine angew. Math.* 199 (1958), pages 23 to 34.
- D. Mumford, *Tata Lectures on Theta I*, Chapter I (theta functions in one variable) and Chapter II (theta functions in several variables).
- D. Mumford, On the equations defining abelian varieties I, *Invent. Math.* 1 (1966), pages 287 to 354.
- D. Mumford, Bi-extensions of formal groups, in *Algebraic Geometry* (Bombay Colloquium 1968), Oxford University Press 1969, pages 307 to 322.
- A. Grothendieck, *Groupes de Monodromie en Géométrie Algébrique (SGA 7 I)*, Lecture Notes in Mathematics 288, Exposés VII and VIII (biextensions).
- H. Weyl, *The Classical Groups*, Chapter II, §4 (the Capelli identity).
- S. Caracciolo, A. D. Sokal and A. Sportiello, Algebraic/combinatorial proofs of Cayley-type identities for derivatives of determinants and pfaffians, *Adv. in Appl. Math.* 50 (2013), pages 474 to 594.
