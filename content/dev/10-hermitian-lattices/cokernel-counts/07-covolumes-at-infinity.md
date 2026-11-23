---
title: Covolumes of the unipotent lattice at infinity
decls:
  - Formalism.L2.SG.Pf.NcReal.JX.CovB.rowBlockCovol_holds
  - Formalism.L2.SG.Pf.NcReal.JX.CovB.blockCovol_holds
  - Formalism.L2.SG.Pf.NcReal.JX.NOf.nofib_of_fib
  - Formalism.L2.SG.Pf.NcReal.JX.NOf.nofib_of_fibQ
  - Formalism.L2.SG.Pf.NcReal.JX.NOf.nofib_holds
  - Formalism.L2.SG.RowsConc.idOneC_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Covolumes of the unipotent lattice at infinity

The normalizing constant of the theta lift contains the volume of a quotient $N_\infty / N_{\mathcal{O}}$, where $N$ is the unipotent radical of the parabolic subgroup of a Hermitian flag and $N_{\mathcal{O}}$ is its integral points. This section computes that volume. The group $N_\infty$ is filtered by blocks of increasing height, and $N_{\mathcal{O}}$ is a fibred lattice: an element lies in it if and only if each block coordinate, corrected by a function of the lower blocks, lies in a lattice $c_p$ of the block. So the volume is the product of the covolumes of the block lattices, and each covolume is computed by a discriminant. The two main results, the Theorem (Fibred description of the integral unipotent group) and the Theorem (Block covolumes), are used in the step [HypsAlt is nonempty](/step/nonempty-hyps/). The last result of the section, the Theorem (Identity part of the concentrated sum), is used in the step [theta local matching](/step/theta-local-matching/).

Let $E/F$ be a CM extension of degree $2f$ over $\mathbb{Q}$, with discriminant $d_E$ ([kinds of number fields](/learn/number-fields/#kinds-of-number-fields)). Fix a Hida setting: a Hermitian space over $E$ with a flag of rank $r$, a weight $k$, fractional ideals $\mathfrak{a}_1, \dots, \mathfrak{a}_r$ of the flag, and a lattice $L_b$ in each graded piece. For a word $u$, let $N_{\mathcal{O}, \infty}(u)$ be the image of the integral unipotent group in $N_\infty$ and $N_{\infty, U}(u)$ the unipotent group at infinity.

**Definition 8.7.1 (Blocks).** The *blocks* of rank $r$ are the elements of
$$C_r = \bigl(P_r \sqcup \{1, \dots, r\}\bigr) \sqcup \bigl(P_r \sqcup \{1, \dots, r\}\bigr),$$
where $P_r$ is the set of pairs $i < j$ in $\{1, \dots, r\}$. Each block $c$ has a *height* and a real vector space $S_c$: a complex coordinate for each pair (the $X$ block), $k + 1$ complex coordinates for each index (the row block), a complex coordinate for each pair (the $K$ block) and a real coordinate for each index (the $M$ block). Each of these is indexed by the infinite places of $F$. For a word $u$ the *block lattice* $c_p \subseteq S_c$ at block $p$ is:

1. for an $X$ block $(i, j)$, the closure of the image of $\mathfrak{a}_i \mathfrak{a}_j^{-1}$;
2. for the row block $b$, the closure of the rows of $\mathfrak{a}_b L_b$;
3. for a $K$ block $(i, j)$, the closure of the image of $\mathfrak{a}_i \mathfrak{a}_j$;
4. for an $M$ block $a$, the imaginary parts of the skew-Hermitian elements of $\mathfrak{a}_a^2$.

**Definition 8.7.2 (Fibred description).** The integral unipotent group has a *fibred description* if, for every Hida setting and word $u$:

1. $N_{\mathcal{O}, \infty}(u) \subseteq N_{\infty, U}(u)$, and $N_{\mathcal{O}, \infty}(u)$ is closed under products and inverses;
2. there is a family of functions $\tau_p$, one for each block $p$, such that $\tau_p(x)$ depends only on the coordinates of $x$ in blocks of lower height, and an element $x$ lies in the block image of $N_{\mathcal{O}, \infty}(u)$ if and only if $x_p - \tau_p(x) \in c_p$ for every block $p$.

The description says that $N_{\mathcal{O}, \infty}$ is an iterated extension of the block lattices.

The proof goes through the block coordinates of a rational datum. A *rational datum* is a matrix $X_0$, a family $x_s$ of vectors and a matrix $M$, all over $E$, that satisfy the admissibility conditions; it has a block image $\mathrm{blk}_\mathbb{Q}(X_0, x_s, M)$ and a lattice condition $\mathrm{Lat}_\mathbb{Q}$ (the datum comes from an integral unipotent element).

**Theorem 8.7.3 (Fibred description from the rational fibre conditions).** Assume the following two conditions. (a) For every admissible rational datum, $\mathrm{blk}_\mathbb{Q}(X_0, x_s, M)_p - \tau_p(\mathrm{blk}_\mathbb{Q}) \in c_p$ for all $p$ if and only if the datum satisfies the lattice condition. (b) Every block vector $x$ with $x_p - \tau_p(x) \in c_p$ for all $p$ is the block image of an admissible rational datum. Then the integral unipotent group has a fibred description.

Lean: `Formalism.L2.SG.Pf.NcReal.JX.NOf.nofib_of_fib`.

*Proof.* The block map identifies the unipotent group at infinity with the block space, and the integral elements with the admissible rational data that satisfy the lattice condition. Condition (a) shows that such data have block images in the fibred set, and condition (b) shows that each element of the fibred set is a block image. The group properties follow from the dictionary between rational data and integral unipotent elements, together with the rational, Gram and place conditions of that dictionary. $\square$

**Corollary 8.7.4 (Fibred description from the first condition).** Assume condition (a). Then the integral unipotent group has a fibred description.

Lean: `Formalism.L2.SG.Pf.NcReal.JX.NOf.nofib_of_fibQ`.

*Proof.* Condition (b) holds, and the claim is the [Theorem (Fibred description from the rational fibre conditions)](/entry/nofib-of-fib/). $\square$

**Theorem 8.7.5 (Fibred description of the integral unipotent group).** The integral unipotent group has a fibred description.

Lean: `Formalism.L2.SG.Pf.NcReal.JX.NOf.nofib_holds`.

*Proof.* Condition (a) holds: it follows from the description of integral theta elements by their block coordinates. Apply the [Corollary (Fibred description from the first condition)](/entry/nofib-of-fib-q/). $\square$

Now the covolumes. For a block $p$ let $\mathrm{cv}(p)$ be the explicit covolume of the block, a number built from $|d_E|$ and the norm of the ideal of the block.

**Definition 8.7.6 (Block covolume condition).** The block lattices satisfy the *covolume condition* if each $c_p$ is countable and has a measurable fundamental domain in $S_p$, and every measurable fundamental domain of $c_p$ has measure $\mathrm{cv}(p)$.

The Lebesgue measure on $S_p$ is fixed by the standard real and complex coordinates ([measures and integrals](/learn/analysis/#measures-and-integrals)).

**Lemma 8.7.7 (Trace determinant of the row lattice).** Let $(m_1, \dots, m_N)$ be a $\mathbb{Z}$-basis of $\mathfrak{a}_b L_b$, with $N = 2f(k + 1)$. Then
$$\bigl|\det\bigl(\mathrm{Tr}_{E/\mathbb{Q}} \, h(m_i, m_j)\bigr)\bigr| = |d_E|^{k+1} \, N(\mathfrak{a}_b)^{2(k+1)}.$$

Lean: `Formalism.L2.SG.Pf.NcReal.JX.CovB.trDetUnimod_holds`.

*Proof.* Let $(\ell_j)$ be a $\mathbb{Z}$-basis of $L_b$ and $(\ell^\vee_k)$ a $\mathbb{Z}$-basis of the dual lattice $L^\vee$. The key input is the unimodularity identity $|\det(\mathrm{Tr}_{E/\mathbb{Q}} h(\ell^\vee_k, \ell_j))| = 1$. The trace determinant of $\mathfrak{a}_b L_b$ is then the index of $\mathfrak{a}_b L_b$ in its trace dual, and this index is computed from the different of $E$ and the norm of $\mathfrak{a}_b$. $\square$

**Theorem 8.7.8 (Row block covolume).** The row block lattice satisfies the covolume condition.

Lean: `Formalism.L2.SG.Pf.NcReal.JX.CovB.rowBlockCovol_holds`.

*Proof.* The lattice $\mathfrak{a}_b L_b$ has rank $N = 2f(k+1)$ over $\mathbb{Z}$, and $c_b$ is the closure of the image of a $\mathbb{Z}$-basis $(m_i)$. The image of a basis of a full lattice in a real space of dimension $N$ is a lattice, so $c_b$ is countable with a parallelepiped as a fundamental domain. Every measurable fundamental domain of a lattice has the same measure, the absolute value of the determinant of the basis. Its square is the Gram determinant of the trace form, up to the normalization of the measure, which the Lemma (Trace determinant of the row lattice) computes. $\square$

**Theorem 8.7.9 (Block covolumes).** All block lattices satisfy the covolume condition.

Lean: `Formalism.L2.SG.Pf.NcReal.JX.CovB.blockCovol_holds`.

*Proof.* There are four kinds of blocks. The row blocks are the [Theorem (Row block covolume)](/entry/row-block-covol-holds/). The $X$ and $K$ blocks are the images of fractional ideals of $E$ in $\mathbb{C}^{\mathrm{Hom}(F, \mathbb{R})}$, and the $M$ blocks are lattices of skew-Hermitian elements in $\mathbb{R}^{\mathrm{Hom}(F, \mathbb{R})}$. In each case the image of a $\mathbb{Z}$-basis of a full lattice gives a fundamental parallelepiped, and its volume is the value $\mathrm{cv}(p)$. $\square$

The last result is the identity part of a concentrated theta sum. For a word $u$, the terms of the sum are indexed by elements $t$, and the identity terms are those with $t$ in the identity class. Each identity term has an operator $a(t)$ on the space $\mathrm{CM}(c_u)$ of the representation.

**Theorem 8.7.10 (Identity part of the concentrated sum).** Let $X$ and $Y$ be two data that are tied in the concentrated setting, and let $u$ be a word. Then the sum of the identity terms of the concentrated sum at $(u, u)$ is the embedding of the identity operator of $\mathrm{CM}(c_u)$.

Lean: `Formalism.L2.SG.RowsConc.idOneC_holds`.

*Proof.* A strict fundamental domain for $N_{\mathcal{O}, \infty}$ exists. Given one, the diagonal computation on the identity cell shows that the operators $a(t)$ of the identity terms sum to the identity of $\mathrm{CM}(c_u)$. The folding of the sum and the integrality of all terms identify the identity part of the concentrated sum with this sum. $\square$

**Remark 8.7.11 (Formalization).** The proofs of the two fibred description results find their inputs by `first | exact …` chains over many guessed names ([NOfibAsm.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NOfibAsm.lean#L13), lines 13 to 15, 21, 27 and 31). So which lemma supplies condition (b), the dictionary conditions and the lattice dictionary is decided when the file is elaborated, not by the text. The block covolume $\mathrm{cv}(p)$ is given by an explicit function that we did not unfold for the $X$, $K$ and $M$ blocks; the proof of the Theorem (Block covolumes) states their form only in outline. The identity of the Lemma (Trace determinant of the row lattice) is proved from the unimodularity statement $|\det(\mathrm{Tr}\, h(\ell^\vee_k, \ell_j))| = 1$ (CovolBRb.lean:509, proved in TrDetPfH.lean:68). The identity part theorem is assembled from four results (folding, existence of fundamental domains, integrality of all terms, the identity cell computation) that we did not open in detail.
