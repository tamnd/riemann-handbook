---
title: Local duality, Siegel sets, elliptic regularity and a sup-norm bound
decls:
  - GlobalTheory.CompanionTheory.Hypotheses₂.BK.blochKatoLocal
  - GlobalTheory.CompanionTheory.Hypotheses₂.BK.formsL
  - GlobalTheory.CompanionTheory.SiegelRed.siegelCore
  - ZetaZeros.D.EllReg.elliptic_regularity_of_parts
  - UpperTheory.Lit.Tam.tamagawa_local_volume_factor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local duality, Siegel sets, elliptic regularity and a sup-norm bound

This last section collects four inputs. The first is the local theory of Bloch and Kato for $\ell$-adic Galois representations; it is not about automorphic forms, but it is filed with this chapter. The second is reduction theory for unitary groups: Siegel sets cover the adelic quotient, and [cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms) decay rapidly on them. The third is elliptic regularity for systems of linear differential equations. The fourth is a bound for the supremum of a holomorphic section by its Petersson norm.

### The local conditions of Bloch and Kato

Let $\ell$ be a prime, $K$ a finite extension of $\mathbb{Q}_\ell$, and $G_K$ its absolute Galois group. Let $B_{\mathrm{cris}} \subseteq B_{\mathrm{dR}}$ be the period rings of Fontaine, with the filtration $\mathrm{Fil}^\bullet$ of $B_{\mathrm{dR}}$, and $\chi$ the cyclotomic character. Let $V$ be a finite-dimensional continuous representation of $G_K$ over a finite extension $L$ of $\mathbb{Q}_\ell$. Put $D_{\mathrm{dR}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{dR}})^{G_K}$; $V$ is *de Rham* if $\dim_L D_{\mathrm{dR}}(V) = [K : \mathbb{Q}_\ell] \dim_L V$. A continuous $1$-cocycle $c$ is *finite* if $c(g) \otimes 1 = g x - x$ for some $x \in V \otimes B_{\mathrm{cris}}$, and $H^1_f(K, V)$ is the space of finite cocycles modulo coboundaries. A pairing $P : V \times V' \to L$ is a *Tate duality* if it is perfect and $P(gx, gy) = \chi(g) P(x, y)$.

**Theorem 1.8.1 (Local conditions of Bloch and Kato).** Let $\ell$ be a prime, and suppose that the period data are identified with the standard rings $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$, compatibly with the Galois action, the Frobenius, the filtration and the element $t$. Then for every finite extension $K$ of $\mathbb{Q}_\ell$:

1. For de Rham $V$ over $\mathbb{Q}_\ell$, $H^1_f(K, V)$ is finite-dimensional and
$$\dim H^1_f(K, V) = \dim H^0(K, V) + \dim D_{\mathrm{dR}}(V) - \dim\big(D_{\mathrm{dR}}(V) \cap \mathrm{Fil}^0(V \otimes B_{\mathrm{dR}})\big).$$
2. Let $V$ be de Rham and $P : V \times V' \to \mathbb{Q}_\ell$ a Tate duality. A continuous cocycle $a$ of $V$ is finite if and only if the cup product $P(a \cup b)$ is a coboundary for every finite cocycle $b$ of $V'$; and the same holds with $V$ and $V'$ exchanged.
3. The integral form of part 2 holds for $\mathbb{Z}_\ell$-lattices $T \subseteq V$, $T' \subseteq V'$ in duality, with the divisible cocycles of $V'/T'$ in place of the cocycles of $V'$.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.BK.blochKatoLocal`.

So $H^1_f(K, V)$ and $H^1_f(K, V')$ are exact annihilators of each other under local Tate duality. The proof uses eight facts on cocycles.

**Proposition 1.8.2 (Eight facts on local cocycles).** Assume local Tate duality and the local Euler characteristic formula for finite $\mathbb{Z}/\ell^r$-modules with continuous $G_K$-action. Then, for representations over finite extensions $L$ of $\mathbb{Q}_\ell$ with lattices over the integers of $L$:

1. the cocycles of $T/\varpi^r T$ form a finite set;
2. a $2$-cochain $z$ with $\varpi^r z$ integral that is a coboundary modulo $\mathcal{O}_L(1)$ is, modulo $\mathcal{O}_L(1)$, the coboundary of a cochain $f$ with $\varpi^r f$ integral and $f$ locally constant modulo $\mathcal{O}_L(1)$;
3. the cup product pairing modulo $\varpi^r$ identifies each subspace between the coboundaries and the cocycles with its double annihilator;
4. the same holds for the divisible cocycles of $V'/T'$;
5. a continuous $2$-cocycle $z$ of $L(1)$ is a coboundary if and only if every multiple $a z$ is a coboundary modulo $\mathcal{O}_L(1)$;
6. the classes of $2$-cocycles of $L(1)$ form a line: if $z$ is not a coboundary, each $z'$ is $a z$ plus a coboundary;
7. the cup product $H^1(V) \times H^1(V') \to H^2(L(1))$ is nondegenerate on both sides;
8. if $S$ and $S'$ are orthogonal subspaces between the coboundaries and the cocycles with $\dim H^1(V) \le \dim S/B^1 + \dim S'/B^1$, then each is the annihilator of the other.

Lean: `GlobalTheory.CompanionTheory.Hypotheses₂.BK.formsL`.

*Proof.* Fact 1 follows from the two assumptions, fact 2 from local Tate duality, and fact 3 from local Tate duality and fact 2. Fact 4 follows from facts 1 and 3, and fact 5 from facts 1 and 2. Local Tate duality gives that $H^2$ with coefficients $\mathbb{Z}/\ell^r(1)$ is cyclic of order $\ell^r$; with fact 5 this gives fact 6. Facts 4 and 5 give fact 7, and facts 1, 6 and 7 give fact 8. $\square$

*Proof of the theorem.* Local Tate duality and the Euler characteristic formula are proved for finite coefficients, so the proposition applies; we use facts 4, 5 and 8. With the identification of the period rings, the dimension formula for $H^1_f$ holds over every coefficient field $L$, and the Euler characteristic bound $\dim H^1(V) \le \dim H^0(V) + \dim H^0(V') + [K : \mathbb{Q}_\ell]\dim V$ holds for dual pairs. The finite cocycles of $V$ and $V'$ are orthogonal under the cup product, and by the dimension formula for $V$ and $V'$ the hypothesis of fact 8 holds, so they are exact annihilators. This gives part 2 over all coefficient fields; with facts 4 and 5 it gives part 3. Part 1 is the dimension formula with $L = \mathbb{Q}_\ell$. $\square$

### Siegel sets for unitary groups

Let $E/F$ be a CM extension with conjugation $\sigma$, $J$ a nondegenerate Hermitian $n \times n$ matrix over $E$, and $G = U_J(\mathbb{A}_F)$, with rational points $G(F)$. A *Witt frame* of rank $r$ is a pair of $n \times r$ matrices $X$, $Y$ over $E$ with $X^* J X = 0$, $Y^* J Y = 0$, $X^* J Y = 1$, such that the Hermitian form is anisotropic on the vectors $z$ with $X^* J z = Y^* J z = 0$. Let $P_0$ be the stabilizer of the flag spanned by the columns of $X$, $P_0^1 \subseteq P_0$ the elements whose diagonal blocks have adelic norm $1$, and for $t$ in the cone
$$C_c = \{t \in \mathbb{R}^r : t_i > 0,\ c\, t_{i+1} \le t_i,\ c \le t_r\}$$
let $a(t)$ be the archimedean torus element that scales the columns of $X$ by $t$ and those of $Y$ by $t^{-1}$. The *Siegel set* is $\mathfrak{S}(\Omega, c, K) = \Omega\, a(C_c)\, K$ for compact $\Omega \subseteq P_0^1$ and a compact subgroup $K$. A function $\varphi$ on $G$ is *smooth of moderate growth* if it is left $G(F)$-invariant, right invariant under an open subgroup of the finite part, continuous, smooth along products of one-parameter subgroups at the archimedean places, and if there is $N$ such that each iterated derivative along such subgroups is bounded by a constant times $\|g\|^N$, where $\|\cdot\|$ is the height. It is *cuspidal* if its constant term along the unipotent radical of every isotropic subspace is $0$.

**Theorem 1.8.3 (Siegel sets for unitary groups).** For every CM extension $E/F$, nondegenerate Hermitian $J$ and Witt frame $(X, Y)$, there are a compact subgroup $K$, a compact $\Omega \subseteq P_0^1$ and $c > 0$ such that:

1. $G = P_0 K$, and $K$ is in good position: each element of $P_0 \cap K$ is a product $m u$ with $m$ in the Levi subgroup and $u$ in the unipotent radical, both in $K$;
2. $G = G(F)\, \mathfrak{S}(\Omega, c, K)$;
3. there is a compact set containing $a^{-1} p a$ for all $p \in \Omega$ and torus elements $a = a(t)$, $t \in C_c$;
4. there are $C$ and $A$ with $\|g\| \le C \|\gamma g\|^A$ for $g \in \mathfrak{S}(\Omega, c, K)$ and $\gamma \in G(F)$;
5. every cuspidal $\varphi$ that is smooth of moderate growth decays rapidly on $\mathfrak{S}(\Omega, c, K)$: for each $N$, $|\varphi(g)|\, \|g\|^N$ is bounded there.

Lean: `GlobalTheory.CompanionTheory.SiegelRed.siegelCore`.

*Proof.* At the archimedean places there is a compact subgroup $K_\infty$ with an Iwasawa decomposition $G_\infty = (P_0 \cap G_\infty) K_\infty$ and with $P_0 \cap K_\infty$ in the Levi subgroup. At the finite places there is a compact subgroup $K_f$ with $G_f = (P_0 \cap G_f) K_f$ that is in good position. These two subgroups assemble to a compact $K$ that satisfies part 1. With this $K$, the [covering statement](/entry/unitary-siegel-domain-exists/) gives $\Omega$ and $c$ with part 2. Parts 3, 4 and 5 hold for any compact $\Omega \subseteq P_0^1$ and $c > 0$, by separate statements. $\square$

### Elliptic regularity

Let $U \subseteq \mathbb{R}^d$ be open. A *system* is a finite family of operators $P_i = \sum_{|w| \le m_i} a_{i,w}(x)\, \partial^w$, where $w$ runs over words in the coordinate directions. Its formal transpose is $P_i^t \phi = \sum_{|w| \le m_i} (-1)^{|w|} \partial^w (a_{i,w} \phi)$, and its principal symbol is $p_i(x, \xi) = \sum_{|w| = m_i} a_{i,w}(x)\, \xi^w$. The system is *elliptic* on $U$ if for each $x \in U$ and $\xi \neq 0$ some $p_i(x, \xi) \neq 0$. A function $u$ is a *weak solution* on $U$ if $\int u\, P_i^t \phi = 0$ for all $i$ and all smooth $\phi$ with compact support in $U$.

**Theorem 1.8.4 (Elliptic regularity).** Let the coefficients $a_{i,w}$ be smooth on $U$ and the system be elliptic on $U$. Then every continuous weak solution $u$ on $U$ is smooth on $U$.

Lean: `ZetaZeros.D.EllReg.elliptic_regularity_of_parts`.

*Proof.* For a cutoff $\chi$ say $\chi u \in H^s$ if $\int (1 + |\xi|^2)^s |\widehat{\chi u}(\xi)|^2 d\xi < \infty$. It suffices that each $x_0 \in U$ has a cutoff $\chi$, equal to $1$ near $x_0$, with $\chi u$ smooth. A continuous function with compact support lies in $H^{-d-1}$, and a function with compact support in every $H^s$, $s \in \mathbb{N}$, is smooth. So it suffices to prove the step: there is $r > 0$ with $B(x_0, r) \subseteq U$ such that, if $\chi u \in H^s$ for all cutoffs supported in $B(x_0, r)$, then $\chi u \in H^{s+1}$ for all of them. Then $s + d + 1$ applications of the step from $-d - 1$ give every $H^s$.

For the step, freeze the leading coefficients at $x_0$. The ellipticity gives $c > 0$ with $c |\xi|^{2k} \le \sum_i |\xi|^{2(k - m_i)} |p_i(x_0, \xi)|^2$, where $k = \max_i m_i$. Testing the weak equation against $\chi$ times exponentials gives an identity for $p_i(x_0, \xi)\, \widehat{\chi u}(\xi)$: it equals convolutions of the Fourier transforms of the error terms $\psi(x)(a_{i,w}(x) - a_{i,w}(x_0))$ and of the lower-order terms with $\widehat{\chi u}$ and $\widehat{\chi' u}$, where $\chi'$ is a second cutoff equal to $1$ on the support of $\chi$. The $L^1$ norm of the Fourier transform of the error term is at most $C r$ for small $r$. A convolution bound with weights $(1 + |\xi|^2)^{s/2} (1 + \varepsilon^2 |\xi|^2)^{-M/2}$ then controls the weighted norm of order $s + 1$ by the norm of order $s$, uniformly in $\varepsilon \in (0, 1]$. These norms are finite for $\varepsilon > 0$, and letting $\varepsilon \to 0$ gives $\chi u \in H^{s+1}$. $\square$

### A sup-norm bound for holomorphic sections

Let $X_k$ be a finite family of frame domains, each with a discrete group $\Gamma_k$, a weight $\lambda_k$ and a pointwise norm $|P(y)|_{\lambda}$ on sections. A family $P = (P_k)$ of holomorphic sections of weight $\lambda$ has the sup norm $\|P\|_\infty = \sup_{k, y} |P_k(y)|_\lambda$ and the Petersson norm $\|P\|_2$, the $L^2$ norm of $|P|_\lambda$ over the adelic quotient for the probability measure, transported to the frames by a fixed dictionary.

**Theorem 1.8.5 (Sup norm and Petersson norm).** Assume the standing laws of the frame data and a good embedding $\sigma$ of the coefficient field. Let $\lambda$ have spread at most $w > 0$, and let the character of $\lambda$ be trivial on each $\Gamma_k$. Then every holomorphic section $P$ of weight $\lambda$ satisfies
$$\|P\|_\infty^2 \le C(E, r, d, M, w)\, \|P\|_2^2,$$
with $C$ a local mean-value constant times a mass of level $M$.

Lean: `UpperTheory.Lit.Tam.tamagawa_local_volume_factor`.

*Proof.* For each $k$ choose an orthogonal base point $x_k$ and a fundamental set $\mathcal{F}_k$, with volume $\mu(\mathcal{F}_k)$. Put $\Phi_k = |P_k|_\lambda^2$ on the domain and $0$ outside. It is measurable, $\Gamma_k$-invariant, and right invariant under the Borel subgroup. For such functions the integral over the adelic quotient, times $S = \sum_k \mu(\mathcal{F}_k)$, equals $\sum_k \int_{\mathcal{F}_k} \Phi_k$. So $\sum_k \int_{\mathcal{F}_k} \Phi_k = \|P\|_2^2\, S$, and the [mass comparison](/entry/plug-comp/) bounds $S$ by the mass of level $M$. A local mean-value inequality bounds $|P_k(y)|_\lambda^2$ by the local constant times $\int_{\mathcal{F}_k} \Phi_k$ for each $y$ in the domain. If the local constant is negative, this gives $P_k(y) = 0$. In both cases $|P_k(y)|_\lambda^2 \le C\, \|P\|_2^2$, and the supremum over $k$ and $y$ gives the theorem. $\square$

**Remark 1.8.6 (Formalization).** We opened the proofs of the five theorems of this section, but not those of their inputs, whose statements we read. For Bloch and Kato, the eight facts are `finZQ`, `topInj`, `dualQ`, `dualDL`, `cobLO`, `topLine`, `nondegLL` and `dualLOf` in `GlobalTheory.CompanionTheory.Hypotheses₂.BK`, and the dimension formula is `GlobalTheory.CompanionTheory.BKDim.bkADim_of_tied`. Part 4 of the Siegel theorem is `GlobalTheory.T.cusp_form_siegel_bound`, which has no cusp form in it despite its name, and part 5 is `GlobalTheory.T.cusp_form_rapid_decay`. Elliptic regularity is assembled from fifteen named inputs by `ZetaZeros.D.EllReg.internal_of_all` and `stepOfParts_of`. The last theorem has a misleading name: it is a sup-norm bound, not a statement about Tamagawa volumes. It also takes a hypothesis `True` and a hypothesis `GlobalTheory.UCls.TorusBound` that its proof does not use. Its main inputs are `GlobalTheory.SupModel.comp_bound` (the mean-value inequality) and `GlobalTheory.T.adelicProbability_eq_normalised_fundamentalSets` (the unfolding).

## Notes and references

The finiteness theorems of this chapter feed the step on [every character](/step/every-character/): they give finite-dimensional spaces of automorphic forms with fixed level, $K$-types and infinitesimal character, and the local results identify representations by their local data. The finiteness theorem is Theorem 1 of Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62 (1968); the adelic form used here follows Moeglin and Waldspurger, *Spectral Decomposition and Eisenstein Series* (1995), Chapter I, and Borel and Jacquet, "Automorphic forms and automorphic representations", Proc. Sympos. Pure Math. 33, Part 1 (1979), 189 to 202. Analytic vectors are from Nelson, "Analytic vectors", Ann. of Math. 70 (1959), 572 to 615, and lowest $K$-types from Schmid, "Some properties of square-integrable representations of semisimple Lie groups", Ann. of Math. 102 (1975), 535 to 564. The Capelli identity is in Howe and Umeda, "The Capelli identity, the double commutant theorem, and multiplicity-free actions", Math. Ann. 290 (1991), 565 to 619. For Whittaker functionals and the mirabolic subgroup see Bernstein and Zelevinsky, "Representations of the group $GL(n,F)$ where $F$ is a non-archimedean local field", Russian Math. Surveys 31:3 (1976), 1 to 68; for the local functional equation, Jacquet, Piatetski-Shapiro and Shalika, "Rankin-Selberg convolutions", Amer. J. Math. 105 (1983), 367 to 464; and for the local converse theorem, Henniart, "Caractérisation de la correspondance de Langlands locale par les facteurs $\varepsilon$ de paires", Invent. Math. 113 (1993), 339 to 350. Hecke L-functions are in Neukirch, *Algebraic Number Theory*, Chapter VII, §§7 to 8. The local conditions are from Bloch and Kato, "L-functions and Tamagawa numbers of motives", The Grothendieck Festschrift I (1990), 333 to 400, §3. Siegel sets for adele groups are in Borel, "Some finiteness properties of adele groups over number fields", Publ. Math. IHES 16 (1963), 5 to 30. Elliptic regularity through Sobolev spaces is in Folland, *Introduction to Partial Differential Equations*, 2nd ed., Chapter 6.
