---
title: The Schrödinger model of the split unitary group
decls:
  - GlobalTheory.KSp.Exist.exists_isKW
  - GlobalTheory.T.exists_weil_representation_split_unitary_schwartzBruhat
  - GlobalTheory.kudlaSplittingSplitUnitary
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Schrödinger model of the split unitary group

This section builds a representation $\omega$ of the split unitary group $\mathrm{U}(n,n)$ on the Schwartz-Bruhat space $S(X)$, $X = M_{m \times n}(E)$, in which the Siegel parabolic acts by the operators $\rho$ of [the big cell relation](/entry/weyl-cell-relation/) and the Weyl element acts by $\kappa\mathcal{F}$. It then proves that $\omega$ is smooth, preserves the $L^2$ norm for each Haar measure, and intertwines the Heisenberg action as the Weil representation does. This is the splitting of the metaplectic cover over $\mathrm{U}(n,n)$ by the character $\chi$, the form in which [Kudla's splitting theorem](/entry/kudla-splitting-split-unitary-of-literature/) is used in the later chapters.

### The extension from the big cell

Keep the notation of the previous two sections: $G = \mathrm{U}(n,n)$, $P$, $w$, $m(a)$, $n(b)$, $\rho$, $\mathcal{F}$, $s$, and the constants $\gamma_0$, $\kappa$ and $C$.

**Lemma 1.4.1 (Extension from the big cell).** Let $G$ and $H$ be groups, $P \subset G$ a subgroup, $w \in G$, $\rho \colon P \to H$ a homomorphism and $W \in H$. Put $\Omega = PwP$. Suppose:

1. if $p, q \in P$ and $wp = qw$, then $W\rho(p) = \rho(q)W$;
2. if $p \in P$ and $wpw \in \Omega$, then there are $p_1, p_2 \in P$ with $wpw = p_1 w p_2$ and $W\rho(p)W = \rho(p_1)W\rho(p_2)$;
3. for each finite set $s \subset G$ there is $u \in G$ with $gu \in \Omega$ for all $g \in s$.

Then there is a homomorphism $\Phi \colon G \to H$ with $\Phi|_P = \rho$ and $\Phi(w) = W$.

*Proof.* First, $f(p_1 w p_2) = \rho(p_1)W\rho(p_2)$ is a well defined function on $\Omega$. If $p_1 w p_2 = q_1 w q_2$, then $w(p_2 q_2^{-1}) = (p_1^{-1}q_1)w$, and condition 1 gives $W\rho(p_2)\rho(q_2)^{-1} = \rho(p_1)^{-1}\rho(q_1)W$, which is the claim. By construction $f(pxq) = \rho(p)f(x)\rho(q)$ for $x \in \Omega$ and $p, q \in P$.

Second, $f(xy) = f(x)f(y)$ when $x$, $y$ and $xy$ lie in $\Omega$. Write $x = p_1 w p_2$ and $y = q_1 w q_2$, and put $p = p_2 q_1$. Then $xy = p_1 (wpw) q_2$, so $wpw \in \Omega$, and condition 2 gives $wpw = r_1 w r_2$ with $W\rho(p)W = \rho(r_1)W\rho(r_2)$. Hence $f(xy) = \rho(p_1 r_1)W\rho(r_2 q_2) = \rho(p_1)W\rho(p)W\rho(q_2) = f(x)f(y)$.

Third, a function on a subset $\Omega$ that is multiplicative in this sense, and for which condition 3 holds, extends to a homomorphism. For $g \in G$ choose $u$ with $u, gu \in \Omega$ and put $\Phi(g) = f(gu)f(u)^{-1}$. For a second choice $u'$, condition 3 applied to a suitable finite set gives $v$ such that the relevant products all lie in $\Omega$; the multiplicativity of $f$ then shows that both choices give the same value. The same device, with one $v$ for $g$, $h$ and $gh$ at once, shows $\Phi(gh) = \Phi(g)\Phi(h)$. For $p \in P$, $\Phi(p) = f(pu)f(u)^{-1} = \rho(p)$. For $w$, choose $u$ with $u, wu \in \Omega$; since $w \in \Omega$ and $f(w) = W$, the second step gives $\Phi(w) = f(w)f(u)f(u)^{-1} = W$. $\square$

**Lemma 1.4.2 (Translation into the big cell).** For each finite set $s \subset \mathrm{U}(n,n)$ there is $u \in \mathrm{U}(n,n)$ with $gu \in PwP$ for all $g \in s$.

*Proof.* Take $u = \begin{pmatrix} 1 & 0 \\ t & 1 \end{pmatrix}$ with $t \in M_n(E)$ Hermitian; it lies in $\mathrm{U}(n,n)$. If $g$ has lower blocks $c_g$ and $d_g$, the lower left block of $gu$ is $c_g + d_g t$. The rows of $(c_g, d_g)$ are independent, so $t \mapsto \det(c_g + d_g t)$ is a polynomial function on the $F$-space of Hermitian matrices that is not $0$. A finite product of such functions is not $0$ on an infinite field, so some $t$ makes all the determinants nonzero. By the criterion in [the big cell relation](/entry/weyl-cell-relation/), each $gu$ lies in $PwP$. $\square$

### The representation

**Theorem 1.4.3 (Weil representation of the split unitary group).** Let $\mu$ be a Haar measure on $X$. There are $\kappa \in \mathbb{C}$ and a representation $\omega$ of $\mathrm{U}(n,n)$ on $S(X)$ such that $\omega(p) = \rho(p)$ for each $p \in P$ and $\omega(w) = \kappa\mathcal{F}$.

Lean: `GlobalTheory.KSp.Exist.exists_isKW` (also `GlobalTheory.T.exists_weil_representation_split_unitary_schwartzBruhat`, a second name).

*Proof.* We check the conditions of the extension lemma with $H$ the group of invertible linear maps of $S$.

The pairing $(x, y) \mapsto \psi(\langle x, y \rangle)$ is a self-dual bicharacter on $X$, since $\langle\ ,\ \rangle$ is a nondegenerate symmetric $F$-bilinear form and $\psi \neq 1$. So $\mathcal{F}$ maps $S$ to $S$, and $\mathcal{F}^2\varphi(x) = C\varphi(-x)$ with $C > 0$. The operators $\rho(p)$ map $S$ to $S$, and $\rho(1) = 1$ and $\rho(pq) = \rho(p)\rho(q)$, so $\rho$ is a homomorphism from $P$. Let $\kappa \neq 0$ be the constant of [the big cell relation](/entry/weyl-cell-relation/) and put $W = \kappa\mathcal{F}$. Then $W^2\varphi(x) = \kappa^2 C\varphi(-x)$ with $\kappa^2 C \neq 0$, and the reflection $\varphi \mapsto \varphi(-\,\cdot)$ maps $S$ onto $S$. So $W$ is injective and onto, that is, $W \in H$.

Condition 1: if $wp = qw$, then $q = wpw^{-1}$ is the Levi element $m((a^*)^{-1})$ when $p = m(a)$, and $\mathcal{F}\rho(p) = \rho(q)\mathcal{F}$ by the substitution $y \mapsto ya$ in the Fourier integral. Condition 2 is [the big cell relation](/entry/weyl-cell-relation/). Condition 3 is the lemma on translation into the big cell. The extension lemma gives $\omega$. $\square$

Since $\omega(m(a)) = \rho(m(a))$ and $\langle x \cdot 0, \cdot \rangle = 0$, one has
$$\omega(m(a))\varphi(x) = \chi(\det a)\, |N_{E/F}(\det a)|_F^{m/2}\, \varphi(xa).$$

To state the Heisenberg property, let $V = M_{m \times 2n}(E)$ and write $v = (v_1, v_2)$ with $v_1, v_2 \in X$. Put
$$\langle\langle v, v' \rangle\rangle = \tfrac12 \operatorname{Tr}_{E/F} \sum_{i,k} Q_{ik}\, (v J v'^*)_{ik}.$$
This is a symplectic form on $V$ over $F$, and $\mathrm{U}(n,n)$ acts on $V$ on the right and preserves it. For $v \in V$ define $h(v)$ on $S$ by
$$h(v)\varphi(x) = \psi\bigl(\langle\langle (x,0), (0,v_2) \rangle\rangle + \tfrac12\langle\langle (v_1,0), (0,v_2)\rangle\rangle\bigr)\, \varphi(x + v_1).$$
These are the operators of the [[Heisenberg group|ZZYCV5EX9J]] of $V$ in the Schrödinger model.

**Theorem 1.4.4 (Kudla's splitting for the split unitary group).** Let $E/F$, $Q$, $\psi$ and $\chi$ be as in [the Gauss integral](/entry/has-gauss-herm/), with $\chi|_{F^\times} = \eta^m$. There is a representation $\omega$ of $\mathrm{U}(n,n)$ on $S(X)$ such that:

1. $\omega$ is smooth: for each $\varphi \in S$ the stabilizer of $\varphi$ is open;
2. for each Haar measure $\mu$ on $X$, each $g$ and each $\varphi$, $\int_X |\omega(g)\varphi|^2\, d\mu = \int_X |\varphi|^2\, d\mu$;
3. for each $g$ and each $v \in V$, $h(v)\,\omega(g) = \omega(g)\, h(vg)$;
4. the Levi element $m(a)$ acts by the formula above.

Lean: `GlobalTheory.kudlaSplittingSplitUnitary`.

This is the case of the split hermitian space of S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), Theorem 3.1: a character $\chi$ of $E^\times$ with $\chi|_{F^\times} = \eta^m$ gives a splitting of the [[metaplectic group|8B0JM2YDE2]] over $\mathrm{U}(n,n)$, and in the Schrödinger model of the Siegel polarization the Levi acts by $\chi(\det a)|\det a|^{m/2}$. See also M. Harris, S. Kudla and W. J. Sweet, *Theta dichotomy for unitary groups*, J. Amer. Math. Soc. 9 (1996), Section 1.

*Proof.* Take the representation of the previous theorem, for one fixed Haar measure. Smoothness, the $L^2$ identity and the Heisenberg relation are checked on the generators $P$ and $w$: for $\rho(p)$ they are direct from the formula, and for $\kappa\mathcal{F}$ they come from the Plancherel formula and the fact that $|\kappa|^2 C = 1$, which follows from $W^2 = \kappa^2 C$ times a reflection together with the unitarity forced by the Heisenberg relation. The Levi formula is the case $p = m(a)$ of $\omega(p) = \rho(p)$, since the quadratic term $\psi(\tfrac12\langle xa, x \cdot 0\rangle)$ is $1$ and $s(\det a) = \chi(\det a)|N(\det a)|_F^{m/2}$. $\square$

By the [Stone-von Neumann theorem](/learn/theta/#the-stone-von-neumann-theorem), property 3 fixes each $\omega(g)$ up to a scalar. So $\omega$ is the [Weil representation](/learn/theta/#the-weil-representation) restricted to $\mathrm{U}(n,n)$ and twisted by a character, and property 4 picks the splitting.

**Remark 1.4.5.** The theorem builds $\omega$ directly on $\mathrm{U}(n,n)$, without the metaplectic group: the extension lemma replaces the cocycle computation. The cost is the relation of the big cell, which needs the constant $\gamma_0$ of the Gauss integral to be nonzero.

**Remark 1.4.6 (Formalization).** The representation is built in `GlobalTheory.KSp.Exist.exists_isKW` (ExistsWeilRepresentationSplitUnitarySchwartzBruh.lean, line 24); the file name is cut short. The extension lemma is `GlobalTheory.bigCell_hom` (ExistsHomOfBigCellGenericRelations.lean, line 51), with the third step `groupChunk_extend` (line 11) of the same file, and the translation lemma is `exists_translate_inCell` (ExistsTranslateInCell.lean, line 69). The output `IsKW` (Definitions/Divisors/UnipVal.lean, line 134) records only the action of $P$ and $w$. In `GlobalTheory.kudlaSplittingSplitUnitary` (KudlaSplittingSplitUnitary.lean, line 17) the Haar measure for $\mathcal{F}$ is the fixed `Measure.addHaar`, and the smoothness, $L^2$ and Heisenberg clauses are separate results (`splitUnitaryWeilRepresentation_isSmooth`, `weil_representation_preserves_L2_space`, `weilRepresentation_intertwines_heisenberg`) whose proofs we have not opened, so the proof of those three clauses above is our sketch. The statement `GlobalTheory.Published.KudlaSplittingSplitUnitary` (PublishedTheorems/TwistedTraceFormula/KudlaSplittingSplitUnitary.lean, line 223) asks for the $L^2$ identity for each Haar measure on the Borel structure, given by an explicit `@Measure ... (borel _)`, and does not state that $\omega$ is unique. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (ExistsWeilRepresentationSplitUnitarySchwartzBruhStatement.lean, line 8).
