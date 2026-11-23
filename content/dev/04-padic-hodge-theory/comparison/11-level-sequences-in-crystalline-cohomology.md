---
title: Level sequences in crystalline cohomology
decls:
  - CrystallineSemistableComparison.Pb.LsQ.seqflat0_pf
  - CrystallineSemistableComparison.Pb.LsG.seq_flat
  - CrystallineSemistableComparison.Pb.LsG.ls_seq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Level sequences in crystalline cohomology

This section proves that the crystalline cohomology of the special fibre of a smooth model, taken over all the truncated Witt rings $W_n(k)$, has the parts of the long exact sequences for $0 \to W_a(k) \to W_c(k) \to W_b(k) \to 0$ that we need. We call this structure a level sequence. The next section uses it, together with finite length at level one ([Theorem 2.10.4](/entry/smooth-model-finite-length-link/)), to show that the limit of the crystalline cohomology over $W_n(k)$ is a finite $W(k)$-module and that its levels have bounded cokernels ([Theorem 2.12.4](/entry/pin-all/)). The proof compares cohomology at level $n$ with cohomology at level $n + 1$ modulo $\ell^n$, on the site of thickenings that are flat over the base.

We keep the notation of the last section. So $(k, \rho, s)$ is a residue datum for $K$, $\mathfrak{X}$ is a model, and $H^j_n(\mathfrak{X})$ is the crystalline cohomology of $\mathfrak{X}$ along $\rho$ over $W_n(k) = W(k)/\ell^n$, that is, the cohomology of the structure functor $\mathcal{O}$ on the site of divided power thickenings over $W_n(k)$. For each $j$ these modules form a system, with the transition maps $r_n : H^j_{n+1}(\mathfrak{X}) \to H^j_n(\mathfrak{X})$ given by reduction modulo $\ell^n$. A *system* of modules over a ring $W$ is a sequence $S_0, S_1, \ldots$ of $W$-modules with $W$-linear maps $r_n : S_{n+1} \to S_n$.

**Definition 2.11.1 (Flat site and its complex).** A divided power thickening over $W_m(k)$ is *flat* if its ring is flat over $W_m(k)$. Let $K_m$ be the complex of $W(k)$-modules whose cohomology is the cohomology of $\mathcal{O}$ on the full subcategory of flat thickenings over $W_m(k)$. Let
$$\mathrm{res}_m : H^j_m(\mathfrak{X}) \to H^j(K_m)$$
be the restriction from all thickenings to flat ones. For a complex $L$ of $W(k)$-modules and $n \geq 0$, let $L/\ell^n$ be the termwise quotient and $\mathrm{pr}_n : L \to L/\ell^n$ the projection.

The flat site is the right place to compare levels. A flat $W_{n+1}(k)$-module $P$ satisfies $P/\ell^n P = P \otimes W_n(k)$ and has no hidden torsion, so the sequence $0 \to P/\ell P \to P \to P/\ell^n P \to 0$, with the first map given by multiplication by $\ell^n$, is exact. For $m = 0$ the base $W_0(k)$ is the zero ring, so $K_0$ is zero.

**Theorem 2.11.2 (Comparison of levels).** Let $(k, \rho, s)$ be a residue datum and $\mathfrak{X}$ a smooth model. There are maps of complexes $\psi_n : K_n \to K_{n+1}/\ell^n$, for $n \geq 0$, such that:

1. $\psi_n$ is bijective on $H^j$ for every $n$ and $j$;
2. for all $n$, $j$ and $x \in H^j_{n+1}(\mathfrak{X})$,
$$\psi_n\big(\mathrm{res}_n(r_n(x))\big) = \mathrm{pr}_n\big(\mathrm{res}_{n+1}(x)\big) \quad \text{in } H^j(K_{n+1}/\ell^n).$$

Lean: `CrystallineSemistableComparison.Pb.LsQ.seqflat0_pf`.

*Proof.* For $n = 0$ both $K_0$ and $K_1/\ell^0$ are zero, so all their cohomology groups are zero. We take $\psi_0 = 0$. Then both conditions hold, since all the groups in them are zero.

Let $n \geq 1$. We take as given that the functor $T \mapsto T/\ell^n T$ sends flat thickenings over $W_{n+1}(k)$ to flat thickenings over $W_n(k)$. Pulling back along this functor gives a map of complexes from $K_n$ to the complex $C$ of the functor $T \mapsto \mathcal{O}(T)/\ell^n$ on flat thickenings over $W_{n+1}(k)$. We take as given that the natural map $K_{n+1}/\ell^n \to C$ is an isomorphism in each degree. Let $\psi_n$ be the pull back $K_n \to C$ followed by the inverse of this isomorphism.

1. *Bijectivity.* It suffices that the pull back $K_n \to C$ is bijective on cohomology. Since $\mathfrak{X}$ is proper and smooth, it has a chart cover $(U_\alpha)$ as in the last section. We take as given that the pull back is bijective on cohomology on each finite intersection of charts, since there it is a computation in coordinates, and that this passes to the site of thickenings that land in some $U_\alpha$. We also take as given that the restrictions from all flat thickenings to those that land in some $U_\alpha$ are bijective on cohomology, at level $n$ and at level $n + 1$ modulo $\ell^n$. The four maps form a commutative square. Three of them are bijective, so the fourth is bijective too.
2. *Compatibility.* After the isomorphism $K_{n+1}/\ell^n \cong C$, both sides of the equation are pullbacks of $x$ from the full site over $W_{n+1}(k)$ to flat thickenings over $W_{n+1}(k)$, with values in $\mathcal{O}/\ell^n$. The left side goes through reduction to level $n$ and the functor $T \mapsto T/\ell^n T$. The right side reduces the values modulo $\ell^n$. The identity of $\mathcal{O}(T)/\ell^n$ is a natural isomorphism between the two composite functors, and we take as given that functors related by a natural transformation that is compatible with the values give the same pullback. So the two sides are equal. $\square$

To pass from one level to the next we need more than the comparison of cohomology. We need that each $K_c$ looks like a complex of free $W_c(k)$-modules.

**Definition 2.11.3 (Flat to level $c$).** A complex $L$ of $W(k)$-modules is *flat to level $c$* if in each degree $i$: $\ell^c$ kills $L^i$; and whenever $a + b = c$ and $x \in L^i$ satisfies $\ell^b x = 0$, then $x \in \ell^a L^i$.

For example, $W_c(k)$ itself is flat to level $c$: an element killed by $\ell^b$ is a multiple of $\ell^{c-b} = \ell^a$. The same holds for every free $W_c(k)$-module, and for every flat one.

**Theorem 2.11.4 (Comparison of levels with reductions).** Let $(k, \rho, s)$ be a residue datum and $\mathfrak{X}$ a smooth model. There are maps of complexes $\psi_n : K_n \to K_{n+1}/\ell^n$ such that:

1. $\psi_n$ is bijective on $H^j$ for every $n$ and $j$;
2. for all $m$, all $b \leq m$ and all $j$, the map $K_m/\ell^b \to K_{m+1}/\ell^b$ induced by $\psi_m$ followed by the reduction $K_{m+1}/\ell^m \to K_{m+1}/\ell^b$ is bijective on $H^j$;
3. $\psi_n(\mathrm{res}_n(r_n(x))) = \mathrm{pr}_n(\mathrm{res}_{n+1}(x))$ for all $n$, $j$ and $x \in H^j_{n+1}(\mathfrak{X})$.

Lean: `CrystallineSemistableComparison.Pb.LsG.seq_flat`.

*Proof.* Take the maps $\psi_n$ of the last theorem. They give parts 1 and 3. We take as given, from the local structure of flat thickenings over $W_c(k)$, that each $K_c$ is flat to level $c$. We also take as given the following fact on complexes: if $L$ is flat to level $m$, $L'$ is flat to level $m + 1$, and $f : L \to L'/\ell^m$ is bijective on cohomology, then for each $b \leq m$ the induced map $L/\ell^b \to L'/\ell^b$ is bijective on cohomology. Apply it with $L = K_m$, $L' = K_{m+1}$ and $f = \psi_m$. This gives part 2. $\square$

**Definition 2.11.5 (Level sequence).** Let $S$ and $S'$ be systems of $W$-modules, and $\ell \in \mathbb{N}$. A *level sequence* for $(S, S')$ consists of $W$-linear maps
$$\rho_{c,b} : S_c \to S_b, \qquad \nu_{a,c} : S_a \to S_c, \qquad \delta_{b,a} : S_b \to S'_a,$$
for all indices, such that for all $a$, $b$, $c$, $n$:

1. $\ell^n$ kills $S_n$;
2. $\rho_{c,c}$ is the identity, and $\rho_{c+1,b} = \rho_{c,b} \circ r_c$ for $b \leq c$;
3. $\nu_{a,c}(\rho_{c,a}(x)) = \ell^{c-a} x$ for $a \leq c$;
4. $r_c \circ \nu_{a+1,c+1} = \nu_{a,c} \circ r_a$ for $a \leq c$, and $r'_a \circ \delta_{b,a+1} = \delta_{b,a}$;
5. if $c = a + b$ and $\rho_{c,b}(x) = 0$, then $x = \nu_{a,c}(y)$ for some $y \in S_a$;
6. if $c = a + b$ and $\delta_{b,a}(x) = 0$, then $x = \rho_{c,b}(y)$ for some $y \in S_c$.

For $S_n = H^j_n(\mathfrak{X})$ and $S'_n = H^{j+1}_n(\mathfrak{X})$, the model is the long exact sequence of the short exact sequence $0 \to W_a(k) \to W_c(k) \to W_b(k) \to 0$ with $c = a + b$, where the first map is multiplication by $\ell^b$:
$$H^j_a \xrightarrow{\ \nu\ } H^j_c \xrightarrow{\ \rho\ } H^j_b \xrightarrow{\ \delta\ } H^{j+1}_a.$$
Conditions 5 and 6 are the inclusions $\ker \rho \subseteq \operatorname{im} \nu$ and $\ker \delta \subseteq \operatorname{im} \rho$. The definition asks for no other part of exactness. The next section uses level sequences only through facts that it takes as given.

**Theorem 2.11.6 (Level sequences).** Let $(k, \rho, s)$ be a residue datum, $\mathfrak{X}$ a smooth model and $j \geq 0$. Then the systems $(H^j_n(\mathfrak{X}))_n$ and $(H^{j+1}_n(\mathfrak{X}))_n$ of $W(k)$-modules have a level sequence.

Lean: `CrystallineSemistableComparison.Pb.LsG.ls_seq`.

*Proof.* Take $\psi_n$ as in the last theorem. For each $i$ define a system $T^i$ by $T^i_n = H^i(K_n)$, with the transition map $T^i_{n+1} \to T^i_n$ equal to $\mathrm{pr}_n$ on $H^i$ followed by the inverse of $\psi_n$ on $H^i$. This is well defined by part 1.

1. *The flat systems have a level sequence.* We take as given the following fact on towers of complexes: if each $K_c$ is flat to level $c$, the maps $\psi_n$ are bijective on cohomology, and the reductions of part 2 of the last theorem are bijective on cohomology, then $(T^j, T^{j+1})$ has a level sequence.
2. *Restriction is an isomorphism of systems.* We take as given that for a smooth model, $\mathrm{res}_m : H^i_m(\mathfrak{X}) \to H^i(K_m)$ is bijective for all $m$ and $i$. By part 3 of the last theorem and the bijectivity of $\psi_n$, the transition map of $T^i$ applied to $\mathrm{res}_{n+1}(x)$ is $\mathrm{res}_n(r_n(x))$. So the inverses of the maps $\mathrm{res}_n$ form an isomorphism of systems from $T^i$ to $(H^i_n(\mathfrak{X}))_n$.
3. *Transport.* A level sequence transports along isomorphisms of systems: conjugate each of $\rho$, $\nu$ and $\delta$ by the isomorphisms. Each condition of the definition is preserved, since it is an equation or an existence statement between linear maps that commute with the transitions.

Apply step 3 to the level sequence of step 1 and the isomorphisms of step 2 for $i = j$ and $i = j + 1$. $\square$

**Remark 2.11.7 (Formalization).** The complex $K_m$ is `Kt` in [ModFSW.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/ModFSW.lean#L34), flatness to level $c$ is `FlatL` and the reduction of part 2 is `qred` in FlatL.lean, and the level sequence is `Tw.LSeq` in [Tens.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/TwistedRepresentations/Tens.lean#L12); that file name has no relation to its content. The first theorem is in [QuoZeroSub.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/QuoZeroSub.lean#L143), with $\psi_n$ for $n \geq 1$ as `psiP` and step 1 as `SubquotientResolution.bij` in BijCov.lean. The other two are in [LsSeqEq.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/LsSeqEq.lean#L21). The facts we take as given are the `GlobalTheory.T` statements `compare_quotient_bijective`, `witt_coord_quotient_pull_bijective`, `witt_level_morphism_cover_compat`, `witt_site_restrict_bijective`, `witt_site_quotient_restrict_bijective`, `pull_eq_of_nat_trans`, `flat_witt_tower_level`, `quotient_reduction_bijective_of_flat`, `lseq_of_flat_tower`, `smooth_model_restriction_bijective` and `lseq_of_level_isos`. Their proofs are in `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`, which we did not open; the reasons we give for them are the usual ones, not a checked reading. The map $\psi_0$ is zero because both sides are zero. `Tw.LSeq` asks only for half of the exactness of the long exact sequence, and constrains $\rho_{c,b}$ only for $b \leq c$.
