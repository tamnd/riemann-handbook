---
title: Row sides and row readings
decls:
  - GlobalTheory.Mem.R3.RowsRead.exists_rowSide
  - GlobalTheory.T.exists_rowForms_adelic_decoratedLattices
  - GlobalTheory.Mem.R3.Rw.PkRead.exists_pkT
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row sides and row readings

The rows of the construction are spaces of definite forms on the row group. Two facts relate them to the rest of the data. First, the forms of each row are matrix coefficients of a coefficient map on decorated lattices, and the finite group, the coefficient tie and the Hecke operators act on them as on flag levels. This is the row side of a tuple. Second, the rows have readings in the coordinates of the definite forms, as stated in [Section 1.15.3](/entry/exists-row-lift-reading-definite-form-coordinates/). In this section we prove the first fact and give the full proof of the second. The row sides enter [the membership and bundles at large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/).

### Row sides

Let $X$ be a stage over a base $B$ with pre-base data $p_x$, and let $I$ be good column input over $B$ whose values lie in the coefficient field. Let $U$ be a set of indices, $X_g$ a finite set of functions on the finite group $G_c$, and $\mathrm{tr}$ a trace datum. These give the family $A = A(X, I, U, X_g, \mathrm{tr})$ of rows, indexed by the tuples $t$ of $(I, U)$. Let $L$ be level and character data for these tuples, with the level of the rows given by $I$ and $U$, and let $e_G : G_c \cong G_0(L)$ be a group isomorphism.

Let $X'$ be the hermitian space of the rows, with Gram matrix $g_{X'}$, and let $\lambda_R$ be the highest weight of the rows at each embedding $\tau$. A coefficient datum $c_X$ is a representation space $W$ with a coefficient map. Let $c_{0R} : V(\lambda_R) \to W$ be a semilinear map over the embedding of $L_L$ into $\mathbb{C}$, and let $g_R = \pm g_{X'}$.

**Definition 1.17.1 (Row side).** A row side for the tuple $t$ consists of three data. The first is a presentation of the forms of the row $A(t)$ by decorated lattice points, with a reduction map $\mathrm{red}$ from the level group $Q$ of $t$. The second is an action tie between $\mathrm{red}$ and the right translations on flag levels. The third is a Hecke tie: the Hecke operators of the row at each inert place act on the presentation as the double coset operators of the rational forms.

**Theorem 1.17.2 (Row sides over decorated lattices).** Let $X$, $I$, $U$, $X_g$, $\mathrm{tr}$, $L$, $e_G$, $c_X$, $g_R$ and $c_{0R}$ be as above. Assume that $c_X$ is a coefficient datum, that $c_{0R}$ is tied to the coefficient map of $c_X$ through the representation $\rho_V$, that
$$\langle c_{0R}(x), c_{0R}(y) \rangle = \mathrm{emb}\big(\mathrm{pair}_{g_R}(x, y)\big)$$
for all $x$ and $y$, that the level index $\beta_X$ of $L$ is $1$, and that the lattice of $X'$ is standard. Then there is a row side $s(t)$ for each tuple $t$, with three properties.

1. For each $q$ in the level group of $t$, $e_G(\mathrm{red}(q))$ is the right translation by the base change of $q$ under the swap of the two embeddings.
2. The presentation of $s(t)$ satisfies the coefficient tie for $c_X$, $c_{0R}$ and $\mathrm{pair}_{g_R}$.
3. There is a Hecke tie for the Hecke operators of the row, at the inert places with labelled and local elements.

In addition the presentations are standard bridges: their extensions to the decorated points agree with the coefficient map.

Lean: `GlobalTheory.Mem.R3.RowsRead.exists_rowSide` (also `GlobalTheory.T.exists_rowForms_adelic_decoratedLattices`, a second name).

*Proof.* Step 1. There is a standard weight cast: a linear map $c$, a family of presentations $P(t)$ of the forms of $A(t)$ by decorated lattices, and the coefficient tie for each $P(t)$. The map $c$ is injective. Step 2. The finite group acts on the row forms through $e_G$ as the right translation on flag levels. This gives the action tie of property 1. Step 3. The split Hecke operators on the rows are the double coset operators of the rational forms. This gives the Hecke operators of $s(t)$. Step 4. At the inert places there is a Hecke tie, which is property 3. Step 5. For the standard bridge, we compare two decorations of a lattice point: the decoration from the presentation and the adelic decoration. With $\beta_X = 1$ the matrix of a point $h$ of the row group in the level environment is $h$ itself, so the point $h$ has an adelic lift $x$ with the same matrix. Then the two decorations agree, and $P(t)$ extends as the coefficient map. $\square$

### The proof of row readings

We recall the setting of [the theorem on row readings](/entry/exists-row-lift-reading-definite-form-coordinates/). Let $D$ be an ambient datum, $G$ a finite group, $A$ a family of level three over $G$, $K_s$ a number field with a map to $L_L$, $R$ a real datum, $F$ a face and $c_G$ a group isomorphism. Assume that each element of the ring $O$ is the image of an element of $K_s$, that the inputs from the literature hold, that $R$ has its pins, and that the condition on the holds is true. Let $y$ be a row datum. Let $m_A(b, \mu)$, for $b$ in $\{0, 1\}$ and $\mu$ a tuple, and $m_L(\mu, j)$ be matrices of definite group forms that satisfy the laws of coordinates, with $m_A(b, y(t)) = r_b(t)$ and $m_L(y(t), i + 1) = l(t, i)$.

**Theorem 1.17.3 (Row readings with the dimension of the multiplicity space).** In this setting there is a reading datum $p$ with $p.m_L = m_L$ and a reading of $y$ with coordinates $m_A$ and $p$. The multiplicity space $M$ of the theta datum at level $J_0$ and character $\chi_0$ of the first row is finite dimensional. Let $D_{\mathrm{all}} = \dim_{\mathbb{C}} M$ and let $n$ be the number of basis vectors of the chain of the first side. Then $p$ carries a number $\delta_p \le 1$ with
$$n = (1 - \delta_p)\, D_{\mathrm{all}}.$$

Lean: `GlobalTheory.Mem.R3.Rw.PkRead.exists_pkT`.

*Proof.* Step 1. The row types of $y$ have a finite set $\Phi$ of representatives. Step 2. Each matrix $m_A(b, \mu)$ and each $m_L(\mu, j)$ has a complexification $s$ with a tie to $m$. This uses that the embedding of $L_L$ commutes with complex conjugation and that the elements of $O$ are integral. Step 3. For each side $b$ there is a chain of levels over the top spaces for $m_A(b, \cdot)$, with a basis and an injective map $j_E$ onto the good part of the multiplicity space. Step 4. Over the definite forms there are lift spaces for $m_L$. Step 5. The reference tuple gives a basis of the rows through the quotient by its stabilizer. Step 6. The multiplicity space $M$ is finite dimensional, by (HF): the theta datum is a family of infinite type, and its level is the level of the inputs. Let $D_{\mathrm{all}} = \dim M$. If $D_{\mathrm{all}} = 0$, then $M = 0$, so the good part is $0$. The map $j_E$ is injective with range the good part, so the chain has no basis vectors and $n = 0$. Put $\delta_p = 0$ in this case, and $\delta_p = 1 - n / D_{\mathrm{all}}$ otherwise. In both cases $\delta_p \le 1$ and $n = (1 - \delta_p) D_{\mathrm{all}}$. The data of Steps 1 to 6 form $p$ and the reading. $\square$

**Remark 1.17.4 (Formalization).** In [ExistsRowFormsAdelicDecoratedLattices.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsRowFormsAdelicDecoratedLattices.lean#L44) the hypothesis that the lattice of $X'$ is standard is taken as `_` at line 57 and is not used. The statement in the theorem above keeps it, because the Lean statement has it. The comparison of decorations of Step 5 is `exists_matEq_ptE` at line 31. The five steps of the row reading proof are statements of the form `GlobalTheory.T.exists_*` that we have not unfolded. In [ExistsRowLiftReadingDefiniteFormCoordinates.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsRowLiftReadingDefiniteFormCoordinates.lean#L19) the finiteness part of the inputs is used directly in Step 6, and the number $\delta_p$ is defined from $n$ and $D_{\mathrm{all}}$, so the relation $n = (1 - \delta_p) D_{\mathrm{all}}$ is a definition and not an estimate.
