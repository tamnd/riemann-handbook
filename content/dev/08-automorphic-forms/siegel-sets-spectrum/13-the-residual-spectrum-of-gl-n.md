---
title: The residual spectrum of GL(N)
decls:
  - PositivityTheory.Rg.Rs.gap_holds
  - PositivityTheory.Rg.Rs.ascAll_holds
  - PositivityTheory.Rg.Rs.ascSeed_of_locSub
  - PositivityTheory.Rg.Rs.ascSeed_holds2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The residual spectrum of GL(N)

Let $E$ be a totally complex number field. This section proves the part of the theorem of Mœglin and Waldspurger that the later chapters use: a discrete automorphic representation $V$ of $GL_N(\mathbb{A}_E)$ with regular integral infinitesimal character embeds into a representation induced from $d$ twists of one unitary cuspidal representation $\pi$ of $GL_a$, with $N = ad$, and at every finite place the local component of $V$ is the Speh representation of the local component of $\pi$. The proof is an induction on $N$ through [constant terms](/learn/automorphic-forms/#constant-terms-and-cusp-forms): an extremal exponent of $V$ cuts $V$ into two smaller [discrete](/learn/automorphic-forms/#the-discrete-spectrum) pieces, and Satake parameters glue the two pieces into one string. A local gap theorem for unitary unramified representations is the key input of the gluing. The result is used for the [step on every character](/step/every-character/), through the rigidity of Satake parameters in archimedean base change.

### Notation

Discrete spaces, exponents $c$ along the parabolic of type $(r, N - r)$, the normalized real part $p(r, c)$ and infinitesimal characters are as in the section on concentration. A cuspidal datum $\pi$ on $GL_a$ is unitary if it is a unitary representation, and normalized if its forms are invariant under the split centre. For a finite place $w$, let $q_w$ be the size of the residue field. A discrete space $V$ has Satake multiset $B$ at $w$ if its unramified vectors at $w$ are nonzero and are Hecke eigenvectors with Satake parameters $B$, unitarily normalized.

For $d \ge 1$ and $0 \le i < d$ put $e_i = \frac{d-1}{2} - i$, so $e_0 > e_1 > \dots > e_{d-1}$ and the $e_i$ are symmetric about $0$.

**Definition 3.13.1 (Regular integral, ascending embedding).** $V$ is regular integral at an embedding $\tau : E \to \mathbb{C}$ if its infinitesimal character at $\tau$ has distinct entries whose differences are integers. An ascending embedding of $V$ for $(\pi, d)$ is an injective equivariant map of $V$ into the space of forms induced from the parabolic with $d$ blocks of size $a$ and from
$$\pi|\det|^{-e_0} \otimes \pi|\det|^{-e_1} \otimes \dots \otimes \pi|\det|^{-e_{d-1}},$$
with normalized induction. The exponents $-e_i$ increase from $-\frac{d-1}{2}$ to $\frac{d-1}{2}$.

The Speh representation $\mathrm{Sp}(\sigma, d)$ of an irreducible representation $\sigma$ of $GL_a(E_w)$ is the unique irreducible quotient of $\sigma\nu^{e_0} \times \dots \times \sigma\nu^{e_{d-1}}$, where $\nu = |\det|$.

### A gap for unitary Satake parameters

**Theorem 3.13.2 (Gap).** Let $V$ be a discrete space on $GL_N$, $w$ a finite place and $B$ a Satake multiset of $V$ at $w$. For every $z \in \mathbb{C}$ with $|z| < q_w^{-1/2}$, the multiplicity of $z$ in $B$ is at most the multiplicity of $q_w z$ in $B$.

Lean: `PositivityTheory.Rg.Rs.gap_holds`.

So a Satake parameter smaller than $q_w^{-1/2}$ is followed by the next parameter of a string. For the trivial representation of $GL_3$ the parameters are $q, 1, q^{-1}$, and $q^{-1}$ is followed by $1$. For $GL_2$ the multiset $\{q^{3/4}, q^{-3/4}\}$ is excluded, because $q^{1/4}$ does not occur; this is the bound $\sigma < \frac12$ for the unramified complementary series.

We use the following facts, taken as given. Let $n + 1 = N$, let $k$ be the residue field, and let $x$ be an unramified vector in a unitary representation of $GL_{n+1}(E_w)$ with a positive invariant Hermitian form $\langle\ ,\ \rangle$.

- (Lattice model.) The translates of $x$ by the lattices between $L$ and $\varpi L$ give vectors $v(M)$, indexed by the subspaces $M$ of $k^{n+1}$. They satisfy $\sum_{\operatorname{codim} M = j} v(M) = \lambda_j v(k^{n+1})$, where $\lambda_j = q^{j(n+1-j)/2} e_j(B)$ and $e_j$ is the $j$-th elementary symmetric function.
- (Operator.) There are a subspace $W$, an operator $U$ with $U(W) \subseteq W$ and $\|Uy\|^2 \ge q^{n-1}\|y\|^2$ on $W$, and vectors $Z_0 = v(k^{n+1}), Z_1, \dots, Z_{n+1} = 0$ in $W$, such that $U Z_j = q^j(\lambda_{j+1} Z_0 - Z_{j+1})$ and $(q^{n+1} - 1)\langle Z_j, Z_0 \rangle = (q^{n+1-j} - 1)\lambda_j \langle Z_0, Z_0\rangle$.
- (Polynomial argument.) For any $q \ge 2$, a positive Hermitian form, a multiset $B$ of $n + 1$ nonzero numbers, and $W$, $U$, $Z_j$ with these properties and $Z_0 \neq 0$, the multiplicity of $z$ in $B$ is at most that of $qz$ whenever $|z| < q^{-1/2}$.

*Proof.* Apply the lattice model to the unramified vector of $V$ at $w$, whose local representation is unitary because $V$ is square integrable. The operator fact gives $W$, $U$ and $Z_j$, and the polynomial argument gives the inequality. $\square$

### Ascending embeddings

**Theorem 3.13.3 (Ascending embeddings).** Let $N \ge 1$ and let $V$ be a discrete space on $GL_N$ that is regular integral at some $\tau$. There are $a, d$ with $ad = N$ and a unitary normalized cuspidal datum $\pi$ on $GL_a$ such that $V$ has an ascending embedding for $(\pi', d)$ for every $\pi'$ isomorphic to $\pi$.

Lean: `PositivityTheory.Rg.Rs.ascAll_holds`.

We use the following facts, taken as given. Throughout, $N = r + s$ with $r, s > 0$, and $V$, $V_1$, $V_2$ are discrete.

- (Dichotomy.) Either $V$ is cuspidal, which is an ascending embedding with $d = 1$, or $V$ has an exponent along some $(r, s)$.
- (Exponents.) $V$ has finitely many exponents, and each has $p(r, c) < 0$.
- (Slices.) For an exponent $c$ along $(r, s)$ there is a nonzero equivariant map $T$ on $V$ that takes the constant term along $(r, s)$ and projects it to the $c$-eigenspace.
- (Chord.) If $p(r, c) = -\lambda rs$ with $\lambda > 0$ and every exponent $c'$ along $(m, N - m)$ has $p(m, c') \le -\lambda m(N - m)$, then the slices of $T$ on the Levi factor are $|\det|^{z_1}$ and $|\det|^{z_2}$ times square integrable forms, with $z_1 = c/(r[E:\mathbb{Q}])$ and $z_2 = -c/(s[E:\mathbb{Q}])$.
- (Projection.) In that case there are $V_1$ on $GL_r$ and $V_2$ on $GL_s$ such that $V$ embeds into the forms induced, without normalization, from $V_1|\det|^{z_1} \otimes V_2|\det|^{z_2}$.
- (Characters.) For such an embedding the infinitesimal character of $V$ is $(m_1 + z_1 - \frac s2) \cup (m_2 + z_2 + \frac r2)$, with $m_i$ that of $V_i$. For an ascending embedding for $(\pi, d)$ it is $\bigcup_i (m_0 + e_i)$, with $m_0$ that of $\pi$.
- (String step.) Assume $V$ embeds as in the projection fact, $V$ is regular integral, $rz_1 + sz_2 = 0$ and $\operatorname{Re} z_1 < \frac s2$, and $V_i$ has an ascending embedding for unitary normalized $(\pi_i, d_i)$. Then $\pi_1 \cong \pi_2$, $z_1 = \frac{s - d_2}{2}$ and $z_2 = \frac{d_1 - r}{2}$.
- (Stages.) If $V$ embeds into the forms induced from $V_1|\det|^{(s - d_2)/2} \otimes V_2|\det|^{(d_1 - r)/2}$ and $V_i$ has an ascending embedding for $(\pi, d_i)$, then $V$ has one for $(\pi, d_1 + d_2)$.

The string step is where the gap is used. At almost all places the Satake multiset of $V$ is the union of two strings $q^{-(z_1 - s/2) - e_i}B_1$ and $q^{-(z_2 + r/2) - e_j}B_2$ built from the Satake multisets $B_i$ of $\pi_i$. Jacquet and Shalika's rigidity theorem compares the cuspidal data; Hermitian symmetry of unitary Satake multisets and the gap force the two strings to join into one; and integrality of the infinitesimal character forces $z_1$ and $z_2$ to be real.

*Proof.* We use strong induction on $N$. If $V$ is cuspidal we take $a = N$ and $d = 1$. Otherwise $V$ has exponents, finitely many, all with $p(r, c) < 0$. Choose one, $c$ along $(r, s)$, for which $\lambda = -p(r, c)/(rs) > 0$ is smallest. Then every exponent $c'$ along $(m, N - m)$ has $p(m, c') \le -\lambda m(N - m)$, so slices and the chord give twisted square integrable slices, and projection gives $V_1$, $V_2$ and an embedding of $V$ into the forms induced from $V_1|\det|^{z_1} \otimes V_2|\det|^{z_2}$.

The infinitesimal characters $m_1$ and $m_2$ are, after shifts, sub-multisets of that of $V$. So $V_1$ and $V_2$ are regular integral at $\tau$, and by induction they have ascending embeddings for unitary normalized $(\pi_1, d_1)$ and $(\pi_2, d_2)$. Now $rz_1 + sz_2 = c/[E:\mathbb{Q}] - c/[E:\mathbb{Q}] = 0$, and $p(r, c) < 0$ gives $\operatorname{Re} c/[E:\mathbb{Q}] < rs/2$, that is, $\operatorname{Re} z_1 < \frac s2$. The string step gives $\pi_1 \cong \pi_2$, $z_1 = \frac{s - d_2}{2}$ and $z_2 = \frac{d_1 - r}{2}$. Stages give an ascending embedding of $V$ for $(\pi', d_1 + d_2)$, for every $\pi'$ isomorphic to $\pi_1$. $\square$

The exponents fit. With $r = d_1 a$ and $s = d_2 a$, the normalized exponents of the two blocks are $z_1 - \frac s2 = -\frac{d_2}{2}$ and $z_2 + \frac r2 = \frac{d_1}{2}$. Then $-e_i(d_1) - \frac{d_2}{2} = -e_i(d)$ and $-e_j(d_2) + \frac{d_1}{2} = -e_{d_1 + j}(d)$ for $d = d_1 + d_2$.

### Local components

**Theorem 3.13.4 (From local subrepresentations).** Assume the following local embedding property: whenever $V$ has an ascending embedding for $(\pi, d)$, $w$ is a finite place, $\sigma$ is the local component of $\pi$ at $w$ and $\sigma'$ that of $V$, there is a nonzero intertwining map
$$\sigma' \to \sigma\nu^{e_{d-1}} \times \sigma\nu^{e_{d-2}} \times \dots \times \sigma\nu^{e_0}.$$
Then the conclusion of the theorem on ascending embeddings holds. Also, if $V$ has an ascending embedding for a unitary normalized $(\pi, d)$, then at every finite place $\sigma' \cong \mathrm{Sp}(\sigma, d)$.

Lean: `PositivityTheory.Rg.Rs.ascSeed_of_locSub`.

We use the following facts, taken as given.

- (Local duality.) Let $\sigma$ and $\sigma'$ be unitarizable irreducible representations over a $p$-adic field of characteristic $0$. If $\sigma'$ has a nonzero map into $\sigma\nu^{e_{d-1}} \times \dots \times \sigma\nu^{e_0}$, then $\sigma\nu^{e_0} \times \dots \times \sigma\nu^{e_{d-1}}$ maps onto $\sigma'$.
- (Segments.) The product $\sigma\nu^{e_0} \times \dots \times \sigma\nu^{e_{d-1}}$ has a unique irreducible quotient. This follows from Zelevinsky's theory of segments and the standard module theorem.

*Proof.* The first part is the theorem on ascending embeddings. For the second, $\pi$ is unitary, so $\sigma$ is unitarizable, and $V$ is square integrable, so $\sigma'$ is unitarizable. The local embedding property gives a nonzero map from $\sigma'$ into the product in increasing order of exponents. Local duality turns it into a surjection from the product in decreasing order onto $\sigma'$. Since $\sigma'$ is irreducible, it is the unique irreducible quotient, which is $\mathrm{Sp}(\sigma, d)$. $\square$

**Theorem 3.13.5 (Residual spectrum).** The conclusion of the previous theorem holds without hypothesis: every discrete space on $GL_N$ that is regular integral at some $\tau$ has an ascending embedding for some unitary normalized $(\pi, d)$, and its local components at the finite places are the Speh representations $\mathrm{Sp}(\pi_w, d)$.

Lean: `PositivityTheory.Rg.Rs.ascSeed_holds2`.

*Proof.* It suffices to prove the local embedding property. Let $\Phi$ be an ascending embedding of $V$. Restricting the forms in $\Phi(V)$ to $GL_N(E_w)$ at a fixed point of the other places gives a nonzero $GL_N(E_w)$-map from $\sigma'$ into a representation induced from $\sigma\nu^{-e_0} \otimes \dots \otimes \sigma\nu^{-e_{d-1}}$, after a projection onto the local component $\sigma$ of each block. Frobenius reciprocity identifies this with a map into the product $\sigma\nu^{e_{d-1}} \times \dots \times \sigma\nu^{e_0}$, since $-e_i = e_{d-1-i}$. The previous theorem then applies. $\square$

**Remark 3.13.6 (Formalization).** The four theorems are `gap_holds` at line 7 of `TopGap.lean`, `ascAll_holds` and `ascSeed_of_locSub` at lines 15 and 20 of `AscSeedOfLocSub.lean`, and `ascSeed_holds2` at line 11 of [AscSeedHolds2.lean](lean:Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/SliceTensors/AscSeedHolds2.lean#L11). The induction is `ascAll_of` at line 49 of [PAscAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/SliceTensors/PAscAll.lean#L49). The theorem `ascAll_holds` does not use the local embedding property, although it sits in the file named after `ascSeed_of_locSub`, and there is no `ascSeed_holds` without the suffix 2. The ascending embedding `AscEmb` is stated with unnormalized induction, so its characters are $|\det|^{(a-1)e_i}$; the Speh quotient `IsSpehOf` uses $|\det|^{(a+1)e_i}$. Both agree with the normalized exponents $\mp e_i$ after the shift by the modulus character $a e_i$. The rigidity input is the published statement `JacquetShalikaRigidity`, passed as a term to `stringStep_of`. The definitions of discrete spaces, `spehExp` and `IsSpehOf` sit in a folder on Galois cohomology of abelian varieties.

## Notes and references

The chapter feeds the spectral side of the comparison of trace formulas and the [step on every character](/step/every-character/), together with the [literature step](/step/every-character-of-literature/). Reduction theory with [Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets) and the [finiteness of automorphic forms](/learn/trace-formula/#finiteness-of-automorphic-forms) are due to Borel and Harish-Chandra, and Borel's book and Harish-Chandra's notes give the adelic form used in the first sections. The equidistribution and the theta means go back to Weil's form of the Siegel formula. The characters of the [real groups](/learn/real-groups/#principal-series-and-the-subrepresentation-theorem) $GL_n(\mathbb{C})$ and the highest weights of their $K$-types are in Parthasarathy, Ranga Rao and Varadarajan. Eisenstein series, their constant terms, the functional equations and the [residual spectrum](/learn/trace-formula/#eisenstein-series-and-the-residual-spectrum) are in Langlands and in Mœglin and Waldspurger; the gallery argument follows Langlands. The residual spectrum of $GL_N$ and the rigidity of isobaric sums are due to Mœglin and Waldspurger and to Jacquet and Shalika. Arthur's lectures survey the whole setting.

- J. Arthur, An introduction to the trace formula, in *Harmonic Analysis, the Trace Formula, and Shimura Varieties*, Clay Math. Proc. 4, Amer. Math. Soc., 2005, 1-263.
- A. Borel, *Introduction aux groupes arithmétiques*, Hermann, Paris, 1969.
- A. Borel and Harish-Chandra, Arithmetic subgroups of algebraic groups, Ann. of Math. 75 (1962), 485-535.
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, Springer, 1968.
- H. Jacquet and J. A. Shalika, On Euler products and the classification of automorphic representations I, Amer. J. Math. 103 (1981), 499-558; II, 777-815.
- R. P. Langlands, *On the Functional Equations Satisfied by Eisenstein Series*, Lecture Notes in Math. 544, Springer, 1976.
- C. Mœglin and J.-L. Waldspurger, Le spectre résiduel de GL(n), Ann. Sci. École Norm. Sup. 22 (1989), 605-674.
- C. Mœglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein Series*, Cambridge Tracts in Math. 113, Cambridge University Press, 1995, Ch. I and II.
- K. R. Parthasarathy, R. Ranga Rao and V. S. Varadarajan, Representations of complex semi-simple Lie groups and Lie algebras, Ann. of Math. 85 (1967), 383-429.
- A. Weil, Sur la formule de Siegel dans la théorie des groupes classiques, Acta Math. 113 (1965), 1-87.
