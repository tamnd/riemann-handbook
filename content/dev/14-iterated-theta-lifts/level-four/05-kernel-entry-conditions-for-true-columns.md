---
title: Kernel entry conditions for true columns
decls:
  - GlobalTheory.LatSCore.latS_at_class
  - GlobalTheory.T.formsLattice_atClass_iff_twistedPolynomial
  - GlobalTheory.KerLatS.kerEntHyp_latS
  - GlobalTheory.T.trueChains_kernelDatum_sourceSideLattice
  - GlobalTheory.Mem.Col2.TC.kerEnt_kform_true
  - GlobalTheory.T.kernelEntries_form_true_chains
  - GlobalTheory.Mem.Col2.TC.kerEntHyp_true
  - GlobalTheory.T.kernelEntryHyp_of_trueColumnChoices
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernel entry conditions for true columns

The kernel datum of a level is a family of $p$-adic power series that move the values of the forms at stage $i$ to the values at stage $i+1$. Before we can build it, we must know four facts about the entries of the kernel at each level-free place: the target pairings have the correct sizes, the lattice at stage $i$ has a description through a source projection, the lattice at stage $i+1$ has the same kind of description through a target projection, and the target projection is the source projection after a twist by a power series and a unit. In this section we prove these four facts for the stage datum of true column choices. The rescaled form of the result is [the kernel entry conditions after scaling](/entry/ker-ent-c-true/). The background on lattices is in Volume 1, at [lattices in quadratic and hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) and [discrete valuation rings and lattices](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices).

### The setting

Let $I$ be a set of true column choices that is in good order and has its pins. Fix laws $l$, a later stage $Z$, and let $D$ be the stage datum of $I$ at $l$ and $Z$. Let $L$ be the coefficient field of $D$. For each place $w$ of $L$ there is an embedding $\iota_w : L \to \mathbb{C}_p$, where $p$ is the residue characteristic of $w$. For each word $u$, each tuple $\mu$ and each stage $i$ we have a lift object $O(u,\mu)$, and a family of place matrices

$$
B_{u,\mu,w,i,c,\tau} \in GL_{N_i}(\mathbb{C}_p),
$$

one for each class $c$ at stage $i$ and each embedding $\tau$. Let $Y$ be a divisor datum for $D$.

**Definition 1.5.1 (Level-free place).** A place $w$ is level free for $u$ and $\mu$ if its residue characteristic is not the level characteristic of $u$, is not one of the two auxiliary primes $g_0$ and $g_1$, and is not one of the primes of $Y$ at $\mu$.

**Definition 1.5.2 (Weight polynomials and the value quotient).** The weight polynomials at stage $i$ are the polynomials over $L$ in the frame variables of rank $N_i$ that have the weights given by the Young diagrams $\nu_i$ of $u$. Evaluation of a weight polynomial at the points of $Y_i$ gives a complex function. The value quotient $V_i$ is the quotient of the weight polynomials by the kernel of this evaluation. So the evaluation $\mathrm{ev}_i : V_i \to \mathbb{C}^{Y_i}$ is injective. We fix a linear section $s_i : V_i \to \mathrm{Pol}_i$.

**Definition 1.5.3 (Canonical map and source projection).** For a function $\varphi$ on the column choices of $\nu_i$, the canonical map sends $\varphi$ to the function $y \mapsto \varphi(\Delta(y))$, where $\Delta(y)$ is the product of the minors of $y$ that the diagrams select. The source function of a polynomial $P$ at the class $c$ is

$$
\begin{aligned}
\mathrm{src}(P)(y) &= \prod_\tau \det(B_\tau)^{-s^\sharp_{i,\tau}} \\
&\quad \cdot \iota_w(P)(B y).
\end{aligned}
$$

It lies in the range of the canonical map. The source projection $\mathrm{pr}^S(c, v)$ is the chosen inverse of the canonical map applied to $\mathrm{src}(s_i(v))$.

**Definition 1.5.4 (Target projection and unit).** The target function uses the matrices $B$ at stage $i+1$ and the exponents $-s^{\mathrm{div}}_{i,\tau}$ in place of $-s^\sharp_{i,\tau}$. The target projection $\mathrm{pr}^T(c', v')(J)$ is the inverse of the canonical map on the target function, evaluated at the column-choice polynomial $\nabla_J$. The unit factor is

$$
\begin{aligned}
u(c,c') &= \lambda(\rho_c) \prod_\tau \det(B_{i,c,\tau})^{s^\sharp_{i,\tau}} \\
&\quad \cdot \lambda(\rho'_{c'}) \prod_\tau \det(B_{i+1,c',\tau})^{-s^{\mathrm{div}}_{i,\tau}},
\end{aligned}
$$

where $\rho_c$ and $\rho'_{c'}$ are the complex constants of the lift object at the two classes and $\lambda$ is the place map from algebraic numbers to $\mathbb{C}_p$. If this product is $0$, we put $u(c,c') = 1$.

**Definition 1.5.5 (The kernel power series).** The power series $\Theta_w(c,c')$ is the $p$-adic image of the kernel series $\mathrm{Th}_i(c,c')$ of the lift object, written in the frames that $B_{i+1}$ and $B_i^{-1}$ give, with the generator values $\mathrm{dgen}(\tau)$ moved to $\mathbb{C}_p$.

**Definition 1.5.6 (Kernel entry conditions).** The kernel entry conditions for $O$, $B$ and $Y$ at a stage datum with forms $\mathrm{fm}$ are the following four statements, for each $u$, $\mu$, each level-free place $w$ and each stage $i < m$.

1. (Values) The target pairings have sizes in the value group of the coefficient field.
2. (Source lattice) A family $\varphi$ of functions on the classes at stage $i$ is the image of an element of the $w$-local lattice of $\mathrm{fm}$ at stage $i$ if and only if $\varphi$ lies in the rational forms $F_i$ and for each class $c$ there is $v \in V_i$ with $\mathrm{ev}_i(v) = \varphi(c)$ and $\|\mathrm{pr}^S(c,v)(\nabla_J)\| \le 1$ for every column choice $J$.
3. (Target lattice) The same statement at stage $i+1$, with the target projection.
4. (Kernel form) If $\mathrm{ev}_{i+1}(v') = K_i(c,c')(\mathrm{ev}_i(v))$, where $K_i$ is the kernel map of the stage, then for each $J$

$$
\begin{aligned}
\mathrm{pr}^T(c',v')(J) &= u(c,c') \\
&\quad \cdot \mathrm{pr}^S(c,v)\bigl(\Theta_w(c,c') \circ G_J\bigr).
\end{aligned}
$$

Here $\Theta_w(c,c') \circ G_J$ is the power series $\Theta_w(c,c')$ evaluated at $0$ along the substitution $G_J$ of the column choice $J$.

In all four results of this section, we assume the following. The primes of $Y$ are those that $I$ allows. The lift objects $O$ are standard for $l$, $Z$ and these primes. Each $B_{u,\mu,w,i,c,\tau}$ is a basis matrix of the lattice of $O(u,\mu)$ at stage $i$ and class $c$, with nonzero determinant. At level-free places, for $i \le m$, every entry of $B$ is $\iota_w(x)$ for some $x \in L$. The kernels of $O$ are unfolded at every stage $i < m$, and the jets of $I$ are in the field. We call these the standing hypotheses.

### The lattice at one class

**Theorem 1.5.7 (The lattice at one class).** Assume the standing hypotheses. Let $w$ be a level-free place for $u$ and $\mu$, let $i < m$, and let $c$ be a class at stage $i$. Let $f$ be a function on $Y_i$ of the form $f(z) = F_1(P)(z)$ for some $P$ in the rational span of the weights $\lambda_i$, where $F_g(P)$ is the function that the Gram matrix of stage $i$, the shift by $\lambda_i$ and the frame $g$ give from $P$. Let $B_m$ be a local basis at $w$ of the lattice of the representative of $c$. Then the following are equivalent.

1. There is $P$ in the $w$-integral span of $\lambda_i$ with $f = F_{g}(P)$, where $g$ is the archimedean image of $B_m^{-1}$.
2. There is $v \in V_i$ with $\mathrm{ev}_i(v) = f$ and $\|\mathrm{pr}^S(c,v)(\nabla_J)\| \le 1$ for every column choice $J$.

Lean: `GlobalTheory.LatSCore.latS_at_class` (also `GlobalTheory.T.formsLattice_atClass_iff_twistedPolynomial`, a second name)

*Proof.* Step 1. We first show that the bound in (2) is a statement about the source function. The source function $\mathrm{src}(s_i(v))$ lies in the range of the canonical map, because the place embeddings at $w$ are onto that range. So the canonical map of $\mathrm{pr}^S(c,v)$ is $\mathrm{src}(s_i(v))$. The Weyl lattice duality theorem states that, for a function $\varphi$ on the column choices of diagrams that fit in rank $N_i$, we have $\|\varphi(\nabla_J)\| \le 1$ for all $J$ if and only if the canonical image of $\varphi$ lies in the Weyl lattice $\Delta_W$ at $p$ for the dual diagrams. The diagrams of $u$ at stage $i$ fit in the source rank. Thus the bound in (2) holds if and only if $\mathrm{src}(s_i(v)) \in \Delta_W$.

Step 2. Assume (1). By the polynomial model step, there is $v \in V_i$ with $\mathrm{ev}_i(v) = f$, because $f$ comes from a rational polynomial. The lattice criterion in integral Weyl coordinates states that, for such $v$, the integral form in (1) holds if and only if $\mathrm{src}(s_i(v)) \in \Delta_W$. So by step 1 the bound in (2) holds for this $v$.

Step 3. Assume (2), with a value $v$. By step 1, $\mathrm{src}(s_i(v)) \in \Delta_W$. By the lattice criterion in integral Weyl coordinates, (1) holds. $\square$

The theorem converts a lattice condition at the archimedean side, which is about integral polynomials in a twisted frame, into a bound at $w$ on a finite set of $p$-adic numbers.

### The source-side lattice

**Theorem 1.5.8 (The source-side lattice condition).** Assume the standing hypotheses and let $l_0$ be a base law for $l$. Then the source lattice condition (2) holds for the twisted stage datum of $I$ at $l$, $l_0$ and $Z$.

Lean: `GlobalTheory.KerLatS.kerEntHyp_latS` (also `GlobalTheory.T.trueChains_kernelDatum_sourceSideLattice`, a second name)

*Proof.* Step 1 (Charts). Fix $u$, $\mu$, a level-free place $w$ and $i < m$. There is a set of bad primes, a type of charts, a chart map on the classes and a family of level charts that read the stage. For $i = 0$ this is the chart reading at stage zero. For $i > 0$ we take the charts of the member step and join them along the middle stage of the tuple chain.

Step 2 (Two forms). The hermitian chart theorem applied to these charts gives two equivalences. The rational one states that a family $\varphi$ is the image of a rational element if and only if $\varphi \in F_i$ and, for each class $c$, $\varphi(c) = F_1(P_c)$ for some $P_c$ in the rational span of $\lambda_i$. The integral one states that a rational element $x$ is in the $w$-local lattice if and only if, for each class $c$ and each local basis $B_m$ at $w$ whose companion is unimodular, $\varphi(c) = F_g(P)$ for some $w$-integral $P$, with $g$ the image of $B_m^{-1}$.

Step 3 (Only if). Let $\varphi$ be the image of $x$ in the $w$-local lattice. The rational form gives $\varphi \in F_i$ and the polynomials $P_c$. Fix a class $c$. The lattice of the representative of $c$ is finitely generated and spans, so it has a local basis $B_m$ at $w$. By the dual lattice criterion, the companion of $B_m$ is unimodular. The integral form gives the integral polynomial for $B_m$. The theorem on the lattice at one class gives the value $v$ with the bound.

Step 4 (If). Assume $\varphi \in F_i$ and the values $v_c$ with the bounds. For each class $c$, the complex value of $v_c$ is a determinant shift of a polynomial in the rational span of $\lambda_i$. So $\varphi(c) = F_1(P_c)$ for such a $P_c$, and the rational form gives $x$ with image $\varphi$. For each class $c$ and each local basis $B_m$ with unimodular companion, the theorem on the lattice at one class, applied to $v_c$, gives the integral polynomial. So the integral form puts $x$ in the $w$-local lattice. $\square$

### The kernel form identity

**Theorem 1.5.9 (The kernel form identity).** Assume the standing hypotheses and let $l_0$ be a base law for $l$. Then the kernel form condition (4) holds for the twisted stage datum of $I$ at $l$, $l_0$ and $Z$.

Lean: `GlobalTheory.Mem.Col2.TC.kerEnt_kform_true` (also `GlobalTheory.T.kernelEntries_form_true_chains`, a second name)

*Proof.* Fix $u$, $\mu$, a level-free place $w$, $i < m$, classes $c$ and $c'$, and values $v$ and $v'$ with $\mathrm{ev}_{i+1}(v') = K_i(c,c')(\mathrm{ev}_i(v))$.

Step 1 (Algebraic constants). Because $O$ is standard, the constants $\rho_c$ and $\rho'_{c'}$ are algebraic numbers. The generator values $\mathrm{dgen}(\tau)$ come from a number field, so they are also algebraic. The determinants of the matrices $B_\tau$ are not zero.

Step 2 (Reduction). The minor product pairing is determined by the canonical map. That is, to prove the identity for every $J$, it is sufficient to give a polynomial $Q$ such that two identities hold: the canonical image of $\mathrm{pr}^S(c,v)$ is $y \mapsto Q(y)$, and the canonical image of the target function is $u(c,c')$ times the action of $\Theta_w(c,c')$ on $Q$. We take

$$
\begin{aligned}
Q &= \prod_\tau \det(B_\tau)^{-s^\sharp_{i,\tau}} \\
&\quad \cdot \iota_w\bigl(P_v\bigr)(B\,y),
\end{aligned}
$$

where $P_v$ is the source polynomial of $s_i(v)$.

Step 3 (Source identity). The product of minors $\Delta(y)$ reads off the columns of $y$. The canonical map of $\mathrm{pr}^S(c,v)$ is $\mathrm{src}(s_i(v))$ by the choice of inverse. When we expand the product $B y$ entry by entry, this function is $Q$.

Step 4 (Target identity). We transport an identity from $\mathbb{C}$ to $\mathbb{C}_p$. Over $\mathbb{C}$, the unfolded kernel of $O$ gives the polynomial identity that the kernel form of $v$ and $v'$ satisfies, with the constant $\rho_c \rho'_{c'}$. The jets of the kernel are algebraic, because the jets of $I$ are in the field, and their lift degrees are bounded. The source polynomial is a weight polynomial, so each monomial in its support has the degrees that the dual diagrams fix. Under these conditions the jet map transport theorem moves the identity to $\mathbb{C}_p$ along $\lambda$. Last, the jet map in the frame of $B_i$ and $B_{i+1}$ is the action of $\Theta_w(c,c')$ in the adapted coordinates.

Step 5 (Scalars). Because the factors are not zero, the unit factor is the product $u(c,c')$ and not the value $1$. The factor $\lambda(\rho_c \rho'_{c'})$ is $\lambda(\rho_c) \lambda(\rho'_{c'})$. The two products of $\det(B_{i,c,\tau})^{\pm s^\sharp_{i,\tau}}$ multiply to $1$. So the scalars on the two sides of the transported identity agree, and the target identity holds. $\square$

### The four conditions

**Theorem 1.5.10 (Kernel entry conditions for true columns).** Assume the standing hypotheses and let $l_0$ be a base law for $l$. Then $O$, $B$ and $Y$ satisfy the kernel entry conditions for the twisted stage datum of $I$ at $l$, $l_0$ and $Z$.

Lean: `GlobalTheory.Mem.Col2.TC.kerEntHyp_true` (also `GlobalTheory.T.kernelEntryHyp_of_trueColumnChoices`, a second name)

*Proof.* The value condition (1) is the theorem on the sizes of target pairings in the value group of the coefficient field. The source lattice condition (2) is the source-side theorem above. The target lattice condition (3) is the target-side lattice theorem for true chains. The kernel form condition (4) is the kernel form identity above. $\square$

The theorem is the input to [the kernel entry conditions after scaling](/entry/ker-ent-c-true/), where the place matrices are rescaled by an adelic unit.

**Remark 1.5.11 (Formalization).** The unit factor `unC` is defined as `unF` when `unF` is not zero and as $1$ otherwise. The proof of the kernel form identity uses the lemma `unF_ne` to remove this case. The theorem `kerEntHyp_latS` introduces the unfolding and jet hypotheses as `_hUnf` and `_hJets` and does not use them ([TrueChainsKernelDatumSourceSideLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TrueChainsKernelDatumSourceSideLattice.lean#L36)). The theorem `kerEnt_kform_true` is stated at the root of its file with an `open ... in` prefix and a full name ([KernelEntriesFormTrueChains.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/KernelEntriesFormTrueChains.lean#L229)). Its proof does not use the hypotheses on the primes of $Y$, on the entries of $B$, on the level-free place or the base law $l_0$. The Weyl lattice duality, the polynomial model step, the lattice criterion in integral Weyl coordinates, the hermitian chart theorem, the dual lattice criterion, the minor product pairing theorem, the jet map transport and the value and target-side theorems are cited through statement files.
