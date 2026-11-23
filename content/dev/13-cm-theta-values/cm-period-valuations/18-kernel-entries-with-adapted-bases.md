---
title: Kernel entries with adapted bases
decls:
  - GlobalTheory.Pdv.kerEntC_true
  - GlobalTheory.T.trueColumnChoices_kernelDatum_adaptedBases
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernel entries with adapted bases

Section 10 used kernel entries that are $C$-entries and have adapted bases. This section shows that such entries exist over a true-column datum. The place matrices are first chosen unitary, so that the kernel hypothesis holds by [the kernel hypothesis over true column choices](/entry/kernel-entry-hyp-of-true-column-choices/). Then each level is rescaled by a unit at the admissible places. The rescaled family keeps the kernel hypothesis, and its theta series are the standard series in the adapted bases. The result is used in [the layer theorem on $C$-entries](/entry/gy-lay-ker-t-ent-c/) of Volume 14.

We keep the notation of Sections 1 and 10: a true-column datum $I$ over a base $B$, laws $l$ and $l_0$, a later stage $Z$, the datum $D = D(l, Z)$ and the twist $\tau_I(l, l_0, Z)$.

### Place data and place matrices

Let $Y$ be divisor data over $D$, and let $O$ assign to each word $u$ and tuple $\mu$ a lift object $O(u, \mu)$ over the twisted chain of $(u, \mu)$. For each level $i$ and class $c$ at level $i$, the object has a lattice $\Lambda_i(c)$ of rank $N(i)$, theta series $\Theta_i(c, c')$ from level $i$ to level $i + 1$, and generator values $d(\tau)$ for each embedding $\tau$. Let $P$ be place data: for each place $w$ of the field of periods it fixes an embedding $\lambda_w$ of $\overline{\mathbb{Q}}$ into $\mathbb{C}_p$, where $p$ is the residue characteristic of $w$.

A *place matrix family* $\mathcal{B}$ assigns to each $(u, \mu, w, i, c, \tau)$ an $N(i) \times N(i)$ matrix over $\mathbb{C}_p$. It is *in order* if each matrix is a basis of the lattice $\tau(\Lambda_i(c))$ at $w$.

A place $w$ is *admissible* if its residue characteristic $p$ is inert in the host, of signal class, or ramified in $d$. The triple $(u, \mu, w)$ is *level free* if the residue characteristic of $w$ is not $T_u$, not a type prime $g_0$ or $g_1$, and not a prime of $\mu$ for $Y$. Two embeddings $\tau$ and $\tau'$ have the *same prime* at $w$ if an integer of the host is small at $\tau$ exactly when it is small at $\tau'$; they have *conjugate primes* if the same holds with $\tau'$ applied to the conjugate. For a matrix $M$ over the host, let $M^\vee = (\overline{M}^{\,t})^{-1}$.

**Definition 5.18.1 (Kernel hypothesis).** The *kernel hypothesis* for $(P, O, \mathcal{B}, Y, \tau)$ says, at every $(u, \mu, w)$ that is level free and every level $i < m$:
1. the target products of the columns at level $i + 1$ have the absolute value of an element of the field of periods;
2. a function at level $i$ comes from the local lattice of the twisted forms at $w$ if and only if it lies in the filtration and all its source products have absolute value at most $1$; the same holds at level $i + 1$ with the target products;
3. the kernel formula: if $v'$ is the image of $v$ under the kernel map, then each target product of $v'$ is a unit $u_C$ times the source product of $v$ at the kernel series applied at $0$.

The products are formed with the matrices of $\mathcal{B}$; they are not unfolded here. A kernel hypothesis gives a kernel entry, the *$C$-entry* of $(P, \mathcal{B})$.

**Definition 5.18.2 (Adapted bases).** A kernel entry $E$ with embeddings $\lambda_w$ has *adapted bases* for $O$ if at every admissible place $w$ and every level free $(u, \mu)$ there are matrices $P_i(c, \tau)$ over the host such that:
1. $\tau(P_i(c, \tau))$ is a basis of $\tau(\Lambda_i(c))$ at $w$, for every $i \le m$;
2. $P_i(c, \tau') = P_i(c, \tau)$ if $\tau$ and $\tau'$ have the same prime;
3. $P_i(c, \tau') = P_i(c, \tau)^\vee$ if they have conjugate primes;
4. for $i < m$, the series of $E$ at $(u, \mu, w, i, c, c')$ is the standard series $\Theta_i(c, c')$, written in the bases $P_i(c)$ and $P_{i + 1}(c')$.

An entry is *in order* for $O$ if, at every level free place, it has a kernel form tie with $O$ whose unit is in order, and it has adapted bases.

### The theorem

**Theorem 5.18.3 (Kernel entries with adapted bases).** Let $I$ be a true-column datum that is in order and has pins. Fix laws $l$, a later stage $Z$ and a law $l_0$ at step $0$. Let $Y$ be divisor data over $D = D(l, Z)$, $O$ lift objects and $P$ place data. Assume:
1. the primes of $Y$ are the primes of $I$;
2. $O$ is the standard object of $I$ at $(l, Z)$ for these primes;
3. every $O(u, a)$ is unfolded at every level $i < m$;
4. the jets of $I$ are in place.

Then there are a place matrix family $\mathcal{B}$ and a kernel hypothesis $h$ for $(P, O, \mathcal{B}, Y, \tau_I(l, l_0, Z))$ such that the $C$-entry of $h$ is in order for $O$.

Lean: `GlobalTheory.Pdv.kerEntC_true` (also `GlobalTheory.T.trueColumnChoices_kernelDatum_adaptedBases`, a second name)

*Proof.* **Unitary bases.** Fix $(w, u, \mu)$ and let $p$ be the residue characteristic of $w$. For each level $i$ and class $c$, a lemma on lattices gives a matrix $G_i(c)$ over the host with $G_i(c)^\vee = G_i(c)$ whose image under $\tau$ is a basis of $\tau(\Lambda_i(c))$ at $w$. Put $P_i(c, \tau) = G_i(c)$ for every $\tau$. Then conditions 1 to 3 of adapted bases hold: condition 2 trivially, and condition 3 since $G_i(c)$ is its own dual. Let $\mathcal{B}_0$ be the family $\tau(P_i(c, \tau))$. It is in order, and its entries are images of elements of the field of periods.

**The kernel hypothesis for $\mathcal{B}_0$.** The standard object is algebraic in its $\rho$-part. With hypotheses 1 to 4, [the kernel hypothesis over true column choices](/entry/kernel-entry-hyp-of-true-column-choices/) gives a kernel hypothesis $h_0$ for $\mathcal{B}_0$.

**Rescaling.** Define
$$
a(w, u, \mu, \tau) =
\begin{cases}
\lambda_w\bigl(d(\tau)\bigr)^{-1} & \text{if } w \text{ is admissible}, \\
1 & \text{otherwise}.
\end{cases}
$$
At admissible places the generator values have absolute value $1$ under $\lambda_w$ by a lemma on lift objects, so $|a| = 1$ everywhere. Let $\mathcal{B}$ multiply the matrix at level $i$ by $a^i$. Then $\mathcal{B}$ is in order, since a basis times a unit is a basis. Each source product and each target product for $\mathcal{B}$ is the product for $\mathcal{B}_0$ times a product of powers of $a$, so it has the same absolute value. The kernel series for $\mathcal{B}$ is the series for $\mathcal{B}_0$ with the variable of $\tau$ scaled by $a(\tau)$, and the unit $u_C$ changes by powers of $a$. A direct computation shows that the kernel formula still holds. This step uses that the canonical maps are onto for $P$, and the algebraic $\rho$-part. So $h_0$ gives a kernel hypothesis $h$ for $\mathcal{B}$.

**Adapted bases.** At an admissible place, $\mathcal{B}$ at level $i$ is $\lambda_w(d(\tau))^{-i}\, \tau(P_i(c, \tau))$ by definition. For such a family, a lemma on $C$-entries shows that the series of the $C$-entry are the standard series in the bases $P_i(c)$. So condition 4 holds.

**Kernel form ties.** At every level free place, the kernel form tie of the $C$-entry with $O$ is built from $\mathcal{B}$ and $h$, and its unit is in order by the algebraic $\rho$-part. $\square$

**Remark 5.18.4 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.trueColumnChoices_kernelDatum_adaptedBases` is a second name, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (TrueColumnChoicesKernelDatumAdaptedBasesStatement.lean:13). The main theorem is stated at top level with its full name, after the namespace of the rescaling lemmas has closed (TrueColumnChoicesKernelDatumAdaptedBases.lean:219).
2. The unitary bases come from `GlobalTheory.Mem.Col2.TC.AdaptedBases.exists_sys`, which puts `fun i c _ => G i c`: the matrices do not depend on $\tau$ (IwasawaDecomposition/NormNatCastEqOne.lean:166). So the conditions on same and conjugate primes are satisfied in the simplest way.
3. The rescaling unit is `GlobalTheory.KerRescale.adUnit` (IwasawaDecomposition/ProdOfMemSupport.lean:173), the rescaled family is `scB` (line 62), and the four effects of rescaling are `prSC_scB`, `prTC_scB`, `thAtW_scB` and `unF_scB` (lines 93, 106, 119 and 141), collected in `kerEntHyp_scB` (line 160). The kernel formula is checked by `linear_combination` (line 212).
4. The fact that the canonical maps are onto, `CanOnto` (Formalism/LocalToGlobal/KernelLattices/ColumnData/KerEntHyp.lean:140), comes from a lemma named `GlobalTheory.T.toy_entPl_canOnto` (IwasawaDecomposition/DominantWeightPolynomialFunctionalMinorsStatement.lean:11). It is a general statement for all $D$ and all place data, in spite of the word "toy" in its name.
5. The kernel hypothesis is `KerEntHyp` with the fields `val`, `latS`, `latT` and `kform` (KerEntHyp.lean:149). Adapted bases are `AdaptedTh` and the condition on $\mathcal{B}$ used in the proof is `AdaptedEnt` (Formalism/LocalToGlobal/KernelLattices/AdaptedEnt.lean:49 and :30); admissible places are `AdPl` (line 23). "In order for $O$" is `EntOk` (Definitions/AutomorphicMembership/FixedVectorEqOfStandardData.lean:114). The products and the kernel series are not unfolded here. Level free is `LevFree` (Formalism/LocalRingCardinality/DataKerI.lean:65).
