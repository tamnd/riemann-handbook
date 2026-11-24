---
title: Local flat maps at split places
decls:
  - GlobalTheory.PartRed.flRow_factor
  - GlobalTheory.T.flatMap_laws_factor_fourierJacobi_source
  - GlobalTheory.LocMod.flatFB_holds
  - GlobalTheory.FlatBFLoc.flatBF_of_laws
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local flat maps at split places

At a place $v$ of $F$ that splits in $E$, the unitary groups become general linear groups, and the Weil representation becomes the natural action on a space of Schwartz-Bruhat functions on matrices. In this model the flat maps of the unfolding become partial Fourier transforms. This section proves that each flat map factors through an explicit partial Fourier transform, the row flat map or the column flat map, and that the factor is again a local model. The two results are inputs of the step [the nonempty hypotheses](/step/nonempty-hyps/), where they compute the local factors of the unfolded periods.

### The row flat map

Let $k$ be a nonarchimedean local field, $\psi$ a continuous nontrivial character of $k$ and $\nu$ a Haar measure on $k$. Let $n, n'$ be finite sets and $c \geq 1$. Consider matrices $t$ with rows indexed by $n \sqcup \{0, \dots, c - 1\}$ and columns indexed by $n' \sqcup \{0, \dots, c\}$. We call the rows in $\{0, \dots, c-1\}$ the lower rows and the columns in $\{0, \dots, c\}$ the right columns. Let $\mathcal{S}$ be the Schwartz-Bruhat space of such matrices over $k$.

**Definition 7.4.1 (Base point, free entries and the row flat map).** For $x_0 \in M_{n \times n'}(k)$, the base point $\beta(x_0)$ is the block matrix with $x_0$ in the upper left block, $1$ at the lower right entries $(l, i)$ with $l = i$, and $0$ elsewhere. For $p \geq 0$, an entry is free for $p$ if it is a lower left entry $(l, s)$ with $l + 1 < p$, an upper right entry $(r, i)$ with $p < i + 1$, or a lower right entry $(l, i)$ with $l < i$. Upper left entries are never free. Put $\mathrm{ch}(t) = \sum_{i=0}^{c-1} t_{i, i+1}$, a sum over lower right entries. For $\Phi \in \mathcal{S}$ let

$$\begin{aligned} E_p \Phi(x_0) &= \int \Phi\bigl(\beta(x_0) + e\bigr)\, \psi\bigl(-\mathrm{ch}(\beta(x_0) + e)\bigr) \, de, \end{aligned}$$

where $e$ runs over the matrices supported on the free entries, with the product of the measures $\nu$. The row flat map sends $\Phi$ to the function on $M_{(n \sqcup \{*\}) \times n'}(k)$

$$\begin{aligned} \mathrm{fl}^{\mathrm{row}}_p \Phi(x) &= E_p\bigl(z \mapsto \Phi(z + R_p(u))\bigr)(x_0), \end{aligned}$$

where $x_0$ is the upper block of $x$, $u$ is its last row, and $R_p(u)$ is the matrix with $u$ in the lower left row $l = p - 1$ and $0$ elsewhere. The column flat map $\mathrm{fl}^{\mathrm{col}}_p$ is defined in the same way, with a column $y$ put in the right column $i = p - 1$ of the upper right block.

The free entries are those that the Fourier-Jacobi unipotent group moves, and $\psi \circ \mathrm{ch}$ is its generic character. So $E_p$ is a twisted integral over an orbit of this group, and the row flat map keeps one row as a free variable.

Let $N_p$ be the unipotent subgroup of $\mathrm{GL}(n \sqcup \{0, \dots, c-1\})$ attached to $p$, and for $g$ in this group let $\sigma(g) = \sum_{i=0}^{c-2} g_{i, i+1}$, the sum over the superdiagonal of the lower right block. For $u \in \mathrm{GL}_c(k)$ let $\mathrm{diag}(1, u)$ be the block matrix with $1$ on $n$ and $u$ on the lower rows.

**Theorem 7.4.2 (Factorization through the row flat map).** Let $\rho \geq 0$ and $c = 2\rho + 1$. Let $M$ be a complex vector space and $L \colon \mathcal{S} \to M$ a linear map with the following four laws.

1. For each upper or lower entry $(r, i)$ in a right column $i \leq \rho$ that is not free for $\rho + 1$, each $b \in k$, and $\Phi'(t) = \psi\bigl(b (t_{r i} - \beta(0)_{r i})\bigr) \Phi(t)$, we have $L \Phi' = L \Phi$.
2. The same holds for each lower left entry $(l, s)$ with $l > \rho$.
3. For each entry $(r, q)$ that is free for $\rho + 1$ and is not in a right column $i \leq \rho$, each $a \in k$, and $\Phi'(t) = \Phi(t + a E_{r q})$, we have $L \Phi' = \psi(\mathrm{ch}(a E_{r q}))\, L \Phi$.
4. For each $u \in \mathrm{GL}_c(k)$ with $\mathrm{diag}(1, u) \in N_{\rho + 1}$, and $\Phi'(t) = \Phi(\mathrm{diag}(1, u)^{-1} t)$, we have $L \Phi' = \psi(-\sigma(\mathrm{diag}(1, u)))\, L \Phi$.

Then there is a linear map $L_0$ on the Schwartz-Bruhat space of $M_{(n \sqcup \{*\}) \times n'}(k)$ such that $L \Phi = L_0 \Psi$ whenever $\Psi$ is a Schwartz-Bruhat function equal to $\mathrm{fl}^{\mathrm{row}}_{\rho + 1} \Phi$.

Lean: `GlobalTheory.PartRed.flRow_factor` (also `GlobalTheory.T.flatMap_laws_factor_fourierJacobi_source`, a second name).

*Proof.* For a set $E$ of entries and a disjoint set $I$ of entries, the partial reduction of $\Phi$ evaluates the entries of $E$ at the base point $\beta(0)$ and integrates the entries of $I$ against $\psi(-\mathrm{ch})$. We say that $L$ kills along $(E, I)$ if $L \Phi = 0$ whenever this partial reduction of $\Phi$ vanishes. For $E = I = \emptyset$ this holds trivially. We enlarge $E$ and $I$ one entry at a time.

An evaluation step adds an entry $e$ to $E$. Suppose $L$ is invariant under multiplication by $\psi(b(t_e - \beta(0)_e))$ for all $b$. By Fourier analysis in the variable $t_e$, a Schwartz-Bruhat function whose restriction to $t_e = \beta(0)_e$ vanishes is a finite sum of differences $\psi(b(t_e - \beta(0)_e))\Phi_j - \Phi_j$. These are killed by $L$, so $L$ kills along $(E \cup \{e\}, I)$. An integration step adds an entry $e$ to $I$. Suppose $L$ transforms under the translations $t \mapsto t + a E_e$ by the character $\psi(\mathrm{ch}(a E_e))$. A function whose twisted integral in the variable $t_e$ vanishes is a finite sum of differences of twisted translates, so again $L$ kills along $(E, I \cup \{e\})$.

We sort the entries for $p = \rho + 1$. The fixed set consists of the entries of laws 1 and 2. The translation set consists of the entries of law 3. The low set consists of the lower right entries $(l, i)$ with $\rho < i \leq l$, and the up set of the lower right entries $(l, i)$ with $l < i \leq \rho$. Laws 1 and 2 give the evaluation steps for the fixed set, and law 3 gives the integration steps for the translation set. For the low set and the up set we use law 4, column by column: a suitable $u$ in $N_{\rho + 1}$ moves an entry of the low set or the up set into entries already treated, and the character $\psi(-\sigma)$ matches the twist. This gives the evaluation steps for the low set and the integration steps for the up set. The entries that remain are the upper left block and the lower left row $l = \rho$. So $L$ kills along (fixed set and low set, translation set and up set), and the partial reduction for these sets is exactly $\mathrm{fl}^{\mathrm{row}}_{\rho + 1}$.

So the kernel of the linear map $F = \mathrm{fl}^{\mathrm{row}}_{\rho + 1}$ lies in the kernel of $L$. Hence $L$ induces a linear map on the image of $F$, and we extend it linearly to the whole Schwartz-Bruhat space of the smaller matrices. This is $L_0$. $\square$

### Local models and the two flat maps

Let $v$ be a place of $F$ split in $E$, with an idempotent of $\mathbb{A}_E$ that selects one place $w$ above $v$, and let $k = E_w$. A frame of a Hermitian space $S$ at $k$ is a basis of $k^{\dim S}$ indexed by a finite set $Y$.

**Definition 7.4.3 (Local model).** Let $S$ and $T$ have frames indexed by $Y'$ and $Y$. A local model for these frames is a linear map $T_m$ from the Schwartz-Bruhat space of $M_{Y \times Y'}(k)$ to functions on $W(S, T)$ such that: each $T_m \Phi$ is a theta function; translation of $\Phi$ by $x$ corresponds to the Heisenberg operator $H(\mathrm{up}(x))$, where $\mathrm{up}(x) \in W(S, T)$ is the image of $x$ at $w$; and multiplication of $\Phi$ by $\psi(\langle \mathrm{up}(t), y \rangle)$ corresponds to $H(y)$, for $y$ supported at the conjugate place.

A local model is the Schrödinger model at $w$, placed inside the space of theta functions. We use three assumptions. The first, the global flat law, says that the flat maps of the global theory are given by absolutely convergent integrals and send theta functions to theta functions. The second, the flat laws at places, says that for every set of places the flat maps satisfy the Heisenberg laws and are equivariant for the Bessel group, for the elements supported at those places. The third, the local Weil law, says: if $\chi_S$ and $\chi_T$ have components $\mu_S$ and $\mu_T$ at $w$, then for $g$ and $h$ supported at $v$ with local matrices $g_k$ and $h_k$,

$$\begin{aligned} \omega(g, h)\, T_m \Phi &= T_m\Bigl( (\mu_S \mu_T^{-1})(\det g_k)\cdot \omega_{\mathrm{loc}}(g_k, h_k)\Phi \Bigr), \end{aligned}$$

where $\omega_{\mathrm{loc}}$ is the action of $\mathrm{GL} \times \mathrm{GL}$ on matrices twisted by $\mu_S^{-1}$.

**Theorem 7.4.4 (Local flat map from Fourier-Jacobi to Bessel).** Assume the global flat law, the flat laws at places and the local Weil law. Let $v, w, k$ be as above, $\nu$ a Haar measure on $k$, and $\psi_k$ the component of $\psi$ at $w$. Let a step from a Jacobi level $W$ of depth $\sigma + 1$ to a Bessel level $V$ of depth $\sigma$ be given, and $s \in k^{\times}$. Let frames of $W_0$, $W$, $A$, $V_0$, $V$ be given, indexed by $n'$, $n' \sqcup \{0, \dots, c\}$, $n$, $n \sqcup \{*\}$, $n \sqcup \{0, \dots, c-1\}$, and adapted to the Jacobi level, the core and the Bessel level with the parameters fixed by $s$. Then for every local model $T_m$ of $(W, V)$ for these frames there is a local model $T_0$ of $(W_0, V_0)$ such that $\flat'(T_m \Phi) = T_0 \Psi$ whenever $\Psi = \mathrm{fl}^{\mathrm{row}}_{\sigma + 1} \Phi$.

Lean: `GlobalTheory.LocMod.flatFB_holds`.

*Proof.* The character $\psi_k$ is continuous and nontrivial, because $\psi$ is the standard character. The Bessel frame forces $c = 2\sigma + 1$. The map $L(\Phi) = \flat'(T_m \Phi)$ is linear, because by the global flat law the flat map is an absolutely convergent integral. We check the four laws of the [Theorem 7.4.2](/entry/fl-row-factor/) for $L$. The multiplication laws for the columns and the rows, the translation law for the free entries and the unipotent law each follow from the Heisenberg laws and the Bessel equivariance of the flat map at $v$, transported to the Schwartz-Bruhat space by the local model and the local Weil law. The factorization theorem gives $L_0$ with $L \Phi = L_0 \Psi$. The same laws show that $L_0$ is a local model for the frames of $W_0$ and $V_0$. $\square$

**Theorem 7.4.5 (Local flat map from Bessel to Fourier-Jacobi).** Assume the global flat law, the flat laws at places and the local Weil law. Let $v, w, k, \nu, \psi_k$ be as above. Let a step from a Bessel level $V$ of depth $\rho$ to a Jacobi level $W$ of depth $\rho$ be given, and $s \in k^{\times}$. Let frames of $A$, $V_0$, $V$, $W_0$, $W$ be given, indexed by $n'$, $n' \sqcup \{*\}$, $n' \sqcup \{0, \dots, c\}$, $n$, $n \sqcup \{0, \dots, c-1\}$, and adapted to the core, the Bessel level and the Jacobi level with the parameters fixed by $s$. Then for every local model $T_m$ of $(V, W)$ for these frames there is a local model $T_0$ of $(V_0, W_0)$ such that $\flat(T_m \Phi) = T_0 \Psi$ whenever $\Psi = \mathrm{fl}^{\mathrm{col}}_{\rho + 1} \Phi$.

Lean: `GlobalTheory.FlatBFLoc.flatBF_of_laws`.

*Proof.* As before, $\psi_k$ is continuous and nontrivial, and the Bessel frame forces $c = 2\rho$. The map $L(\Phi) = \flat(T_m \Phi)$ is linear by the global flat law. The dual laws hold: multiplication laws for the columns and the rows, translation laws for the free entries and a local unipotent law. They come from the Heisenberg laws and the Bessel equivariance at $v$, through the local model and the local Weil law. The column analogue of the factorization theorem gives $L_0$ with $\flat(T_m \Phi) = L_0(\mathrm{fl}^{\mathrm{col}}_{\rho + 1} \Phi)$. The same laws show that $L_0$ takes theta function values, intertwines translations with Heisenberg operators, and intertwines multiplications with Heisenberg operators. So $L_0$ is a local model. $\square$

**Remark 7.4.6 (Formalization).** The factor $L_0$ is obtained by extending a linear map from the image of the row flat map with `LinearMap.exists_extend`, so it is not explicit off that image ([FlatMapLawsFactorFourierJacobiSource.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatMapLawsFactorFourierJacobiSource.lean#L320)). The group $N_p$ and the partial reductions are used through their defining lemmas and are not unfolded here. In the two local theorems the place is a split idempotent of $\mathbb{A}_E$ with a ring projection to $k$. The four laws in each local theorem are quoted from lemmas that are not unfolded here; for the Bessel to Fourier-Jacobi direction, the column factorization is `flatMap_fourierJacobi_factors_local_flat`. The equation $c = 2\rho$ is derived by `omega` from the Bessel frame ([FlatMapBesselToFourierJacobiLocalModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatMapBesselToFourierJacobiLocalModel.lean#L24)).
